import React from 'react';
import ReactDOM from 'react-dom';
import './style.css'

function App() {
    /**
     * Challenge: See if you can do it all again by yourself :)
     */
    const [thingsArray, setThingsArray] = React.useState(['Thing 1', 'Thing 2'])

    function addItem() {
      setThingsArray(function(){
        return [...thingsArray, `Things ${thingsArray.length+1}`]
      })
        // Build from scratch :)
    }
    
    const thingsElements = thingsArray.map(thing => <p key={thing}>{thing}</p>)
    
    return (
        <div>
             <button onClick={addItem}>Add Item</button>
            {thingsElements}
        </div>
    )
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
