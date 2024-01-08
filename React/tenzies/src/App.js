import React from 'react';
import Die from './Die.js'
import Confetti from 'react-confetti';
import {nanoid} from 'nanoid';

export default function App() {

    const [dice, setDice] = React.useState(allNewDice())
    const [tenzies, setTenzies] = React.useState(false) 
    const [rolls, setRolls] = React.useState(0)
    const [startTime] = React.useState(Date.now());
    const [totalTime, setTotalTime] = React.useState(0);
    // create a function that tracks the time taken to win. when the confetti comes out.

    React.useEffect(() => {
        if (tenzies){
            const endTime = Date.now();
            const timeTaken = endTime - startTime;
            console.log(`Time taken on the React website: ${timeTaken}ms`);
            setTotalTime(timeTaken);
        }
    }, [tenzies])

    React.useEffect(() => {
        let numbers = []
        for (let die of dice){
            numbers.push(die.value)
        }
        function allEqual(array) {
            if(array.length <= 1) return true;
            for(let i = 1; i < array.length; i++) {
                if(array[i] !== array[0]) {
                    return false;
                }
            }
            return true;
        }
        const allHeld = dice.every(die => die.isHeld)
        if (allEqual(numbers) && allHeld){
            setTenzies(true)
            console.log("TENZIES")  
        }
    }, [dice]);
    
    function allNewDice(){
        let newDice = [];
        for (let i = 0; i <10;i++){
            let roll = Math.floor(Math.random()*6)+1;
            newDice.push({value: roll, 
                isHeld: false,
                id: nanoid()}); 
        }
        return newDice;
    } 

function newGame() {
    if (tenzies) {
        setTenzies(false);
        setDice(allNewDice())
        setRolls(0);
        setTotalTime(0);
    }
}


    function rollDice(){
        setRolls(prevRolls => prevRolls + 1)
        setDice(oldDice => oldDice.map(die=>{
            return die.isHeld === true ?
                {...die} :
                {value: Math.floor(Math.random()*6)+1,
                isHeld:false,
                id:nanoid()}
        } )) 
    }

    function holdDice(id) {
            setDice(oldDice => oldDice.map(die=> {
                return die.id === id ? 
                    {...die, isHeld: !die.isHeld} :
                    die
            }))
    }



    const diceElements = dice.map(die => 
         <Die key = {die.id} value = {die.value} isHeld = {die.isHeld} holdDice = {()=> holdDice(die.id)}/>
    )

    return (
        <main>
            {tenzies && <Confetti/> }
            <h1 className="title">Tenzies</h1>
            <p className="instructions">Roll until all dice are the same. Click each die to freeze it at its current value between rolls.</p>
            <h1 className='title'>Rolls: {rolls}</h1>
            <h1 className='title'>{tenzies === true ? `Total Time: ${totalTime}ms` : null}</h1>
            <div className="dice-container">
                {diceElements}
            </div>
            <button className="roll-dice" onClick={tenzies ? newGame : rollDice}>{tenzies===true ?  "New Game":  "Roll"}</button>
           
        </main>
    )
}


//ideas: track no. of rolls, track time it took to win, save your best time to localStorage