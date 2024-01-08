            {props.setup && <h3> {props.setup}</h3>}
            {isShown && <p> {props.punchline}</p> } 
            these two code is used to check if props.setup and isShown are both true/exist before running the code that follows
            this is done use the && operator

            CONDITIONAL RENDERING

            terniary operation is good if you want to choose between two different properties for two situations

            1. What is "conditional rendering"?
When we want to only sometimes display something on the page
based on a condition of some sort


2. When would you use &&?
When you want to either display something or NOT display it


3. When would you use a ternary?
When you need to decide which thing among 2 options to display


4. What if you need to decide between > 2 options on
   what to display?
Use an `if...else if... else` conditional or a `switch` statement


function App() {
    let someVar
    if () {
        someVar = <SomeJSX />
    } else if() {
        ...
    } else {
        ...
    }
    return (
        <div>{someVar}</div>
    )
}