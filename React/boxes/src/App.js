import React from "react"
import boxes from "./boxes"
import Box from "./Box"

export default function App() {
    const [squares, setSquares] = React.useState(boxes) 
    
    function toggle(id) {
        setSquares(prevSquares=>{
            return prevSquares.map((square)=>{
                return square.id === id ? {...square, on:!square.on} : square
            })

            // const newSquares = []
            // for (let i=0; i<prevSquares.length; i++) {
            //     const currentSquare = prevSquares[i]
            //     if (currentSquare.id === id) {
            //         const updatedSquare = {...currentSquare, on:!currentSquare.on}
            //         newSquares.push(updatedSquare)
            //     } else {
            //         newSquares.push(currentSquare)
            //     }
            // }
            // return newSquares   
    })}

    const squareElements = squares.map(square => (
        <Box 
        key={square.id} 
        id = {square.id}  
        on={square.on} 
        toggle = {toggle} 
        />
    ))
    //  * 3. In the Box component, apply dynamic styles to determine
    //  *    the backgroundColor of the box. If it's `on`, set the
    //  *    backgroundColor to "#222222". If off, set it to "none"
    //  */ 
    
    return (
        <main>
            {squareElements}
        </main>
    )
}
