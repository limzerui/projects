what cant React handle on its own?
    outside effects:
        localStorage
        api/database interaction
        syncing 2 different internal states
        anyth React isnt in charge of 
    
useEffect() allows us to interact outside of the React ecosystem(state, props, UI)
useEffect() allows us to synchronise state with those outside systems(localStorage, API)

function we passed in useEffect() will run after every render of our component. therefore, if we want to change the state of components inside the useEffect() function, we get caught in a loop 

the dependencies array (the 2nd paramenter to useEffect. note that callback fn is the first parameter). it contains values that if they change from one render to the next, will cauise the useEffect fn to run. in other words, it limits the number of times the effect will run.
therefore, an empty array is not looking for any changes between one render and the next. if it has changed(its different), then will it run useEffect()


1. What is a "side effect" in React? What are some examples?
- Any code that affects an outside system.
- local storage, API, websockets, two states to keep in sync


2. What is NOT a "side effect" in React? Examples?
- Anything that React is in charge of.
- Maintaining state, keeping the UI in sync with the data, 
  render DOM elements


3. When does React run your useEffect function? When does it NOT run
   the effect function?
- As soon as the component loads (first render)
- On every re-render of the component (assuming no dependencies array)
- Will NOT run the effect when the values of the dependencies in the array stay the same between renders


4. How would you explain what the "dependecies array" is?
- Second paramter to the useEffect function
- A way for React to know whether it should re-run the effect function



NOTE: the use of template strings---> `${}`(used at count)