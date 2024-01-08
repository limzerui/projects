// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn Reactnowheheh
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

// App.js
import React from "react"
import Navbar from "./components/Navbar"
import Hero from "./components/Hero"
import Card from "./components/Card"
import data from "./data.js"

export default function App() {
  const cards = data.map(item => {
    return(
      <Card 
          key = {item.id} 
          item = {item}
          // {...item}
          // img = {item.coverImg}
          // rating = {item.stats.rating}
          // reviewCount = {item.stats.reviewCount}
          // location = {item.location}
          // title = {item.title}
          // price = {item.price}
          // openSpots = {item.openSpots}
        />
    )
  })
    return (
      <div>
        <Navbar />
        <Hero />
        <section className="cards-list">
        {cards}
        </section>
      </div>
    )
}