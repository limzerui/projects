import React from "react"
import Joke from "./Jokes"
import jokesData from "./jokesData"

export default function App() {
    const jokeElements = jokesData.map(joke => {
        return <Joke key = {joke.id} setup={joke.setup} punchline={joke.punchline} />
    })
    return (
        <div>
            {jokeElements}
        </div>  
    )
}


// return (
//     <div>
//         {
//             messages.length ===0 ? <h1> caught up</h1> : <h1>you have {messages.length} unread {messages.length >1? "messages": "message"}</h1>
//         }
//     </div>
// )