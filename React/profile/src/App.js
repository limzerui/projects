import React from "react"
import logo from './images/man.png'
import Star from './Star.js'

export default function App() {
    const [contact, setContact] = React.useState({
        firstName: "Johnny",
        lastName: "Doe",
        phone: "+1 (719) 555-1212",
        email: "itsmyrealname@example.com",
        isFavorite: true
    })
    
    
    function toggleFavorite() {
        setContact(prevContact =>({...prevContact, isFavorite: !prevContact.isFavorite}))
        //change setContact.isFavrouite change!
        // setContact(function(){
        // if(contact.isFavorite===true){ contact.isFavorite=false}
        // else{
        //     contact.isFavorite= true
        // }
        // })
    }
    
    
    

    return (
        <main>
            <article className="card">
                <img src={logo} className="card--image" />
                <div className="card--info">
                    <Star 
                    isFilled={contact.isFavorite} handleClick={toggleFavorite} />
                    <h2 className="card--name">
                        {contact.firstName} {contact.lastName}
                    </h2>
                    <p className="card--contact">{contact.phone}</p>
                    <p className="card--contact">{contact.email}</p>
                </div>

            </article>
        </main>
    )
}
