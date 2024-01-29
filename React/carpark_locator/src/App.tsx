"use client";

import React, { useEffect, useState, useRef, useCallback } from "react";
import {
  APIProvider,
  Map,
  AdvancedMarker,
  InfoWindow,
  useMap,
} from "@vis.gl/react-google-maps";
import { MarkerClusterer } from "@googlemaps/markerclusterer";
import type { Marker } from "@googlemaps/markerclusterer";
import proj4 from "proj4";

function App() {
  const [open, setOpen] = useState(false);
  const [position, setPosition] = useState({ lat: 53.54, lng: 10 });
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("http://localhost:3001/api");
      const json = await response.json();

      const convertedData = json.Result.map((item) => {
        let lat, lng;
        if (
          item.geometries &&
          item.geometries.length > 0 &&
          item.geometries[0].coordinates
        ) {
          const coordinates = item.geometries[0].coordinates.split(",");
          const SVY21 =
            "+proj=tmerc +lat_0=1.366666666666667 +lon_0=103.8333333333333 +k=1.0 +x_0=28001.642 +y_0=38744.572 +ellps=WGS84 +units=m +no_defs";
          const WGS84 = "WGS84";
          const convertSVY21ToLatLng = (x, y) => {
            return proj4(SVY21, WGS84, [parseFloat(x), parseFloat(y)]);
          };
          [lng, lat] = convertSVY21ToLatLng(coordinates[0], coordinates[1]);
        } else {
          // Handle the case where coordinates are not available
          lat = 0; // Default value or some error handling
          lng = 0; // Default value or some error handling
        }
        console.log(lng, lat);
        return {
          name: item.carparkNo,
          lat: lat,
          lng: lng,
          key: item.carparkNo,
          lots: item.lotsAvailable,
          type: item.lotType,
        };
      });

      setData(convertedData);
    };

    fetchData();
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          setPosition({
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          });
        },
        (error) => {
          console.error("Error Code = " + error.code + " - " + error.message);
          // Handle location error (e.g., user denied permission)
        }
      );
    } else {
      console.log("Geolocation is not supported by this browser.");
    }
  }, []);

  return (
    <APIProvider apiKey={process.env.REACT_APP_API_KEY}>
      <div style={{ height: "100vh", width: "100%" }}>
        <Map zoom={15} center={position} mapId={"{process.env.PUBLIC_MAP_ID}"}>
          <AdvancedMarker
            position={position}
            onClick={() => {
              setOpen(!open);
              console.log(open);
            }}
          >
            <span style={{ fontSize: "36px" }}> 👇</span>
          </AdvancedMarker>

          {open && (
            <InfoWindow position={position} onCloseClick={() => setOpen(false)}>
              <p>Current Location</p>
            </InfoWindow>
          )}

          {data && <Markers points={data} />}
        </Map>
      </div>
      <div>{data && <pre>{JSON.stringify(data, null, 2)}</pre>}</div>
    </APIProvider>
  );
}

type Point = google.maps.LatLngLiteral & { key: string };
type Props = { points: Point[] };

const Markers = ({ points }) => {
  const map = useMap();
  const [activeMarker, setActiveMarker] = useState(null);
  const clusterer = useRef(null);
  const markersRef = useRef({});

  const handleMarkerClick = useCallback(
    (key) => {
      const markerData = points.find((point) => point.key === key);
      if (markerData) {
        console.log("Marker clicked:", markerData);
        setActiveMarker(markerData);
      }
    },
    [points]
  );

  useEffect(() => {
    if (!map) return;

    if (clusterer.current) {
      clusterer.current.clearMarkers();
    } else {
      clusterer.current = new MarkerClusterer({ map });
    }

    // Update or create new markers
    points.forEach((point) => {
      let marker = markersRef.current[point.key];
      if (!marker) {
        marker = new google.maps.Marker({
          position: point,
          map: map,
        });
        marker.addListener("click", () => handleMarkerClick(point.key));
        markersRef.current[point.key] = marker;
      }
    });

    // Add markers to clusterer
    clusterer.current.addMarkers(Object.values(markersRef.current));

    // Cleanup function
    return () => {
      Object.values(markersRef.current).forEach((marker) =>
        marker.setMap(null)
      );
    };
  }, [map, points, handleMarkerClick]);

  return (
    <>
      {activeMarker && (
        <InfoWindow
          position={{ lat: activeMarker.lat, lng: activeMarker.lng }}
          onCloseClick={() => setActiveMarker(null)}
        >
          <div>
            <p>{activeMarker.name}</p>
            <p>Lots Available: {activeMarker.lots}</p>
            <p>Lot Type: {activeMarker.type}</p>
          </div>
        </InfoWindow>
      )}
    </>
  );
};

export default App;
