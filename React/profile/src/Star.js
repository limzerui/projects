 import React from 'react';

export default function Star(props) {
    let starIcon = props.isFilled ? "goldenstar.png" : "blackstar.png"
    const star = require(`./images/${starIcon}`)
    return(
        <img src= {star} className="card--favorite"
        onClick={props.handleClick } />
    )
/* <img 
                        src={star} 
                        className="card--favorite"
                        onClick={toggleFavorite}
                    /> */

    }
