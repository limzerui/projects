const express = require("express");
const axios = require("axios");
const app = express();
const port = 3001;

app.get("/api", async (req, res) => {
  try {
    // First API request to get the token
    const { data: tokenData } = await axios.get(
      "https://www.ura.gov.sg/uraDataService/insertNewToken.action",
      {
        headers: {
          AccessKey: "d683840b-371b-4c8d-9859-9cbe36b59e5c", // replace with your actual access key
        },
      }
    );

    // Check if the token request was successful
    if (tokenData.Status !== "Success") {
      throw new Error("Failed to get token");
    }

    // Second API request using the token
    const apiResponse = await axios.get(
      "https://www.ura.gov.sg/uraDataService/invokeUraDS?service=Car_Park_Availability",
      {
        headers: {
          AccessKey: "d683840b-371b-4c8d-9859-9cbe36b59e5c", // replace with your actual access key
          Token: tokenData.Result, // use the token from the first request
        },
      }
    );

    // Log the response to the console
    console.log(apiResponse);

    // Send the data from the second API request
    res.json(apiResponse.data);
  } catch (error) {
    res.status(500).json({ error: error.toString() });
  }
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
