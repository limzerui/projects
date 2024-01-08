import React from "react"

export default function Joke(props) {
    const [isShown, setIsShown] = React.useState(false)

    function toggleShown  () { 
        console.log(isShown)
        setIsShown(prev => !prev)
    }
    return (
        <div >
            {props.setup && <h3> {props.setup}</h3>}
            {isShown && <p> {props.punchline}</p> }
            <button onClick={toggleShown}>{isShown? "Hide" : "Show"} Punchline</button>
            
            <hr />
        </div>
    )
}