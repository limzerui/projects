import React from "react"
import Sidebar from "./components/Sidebar"
import Editor from "./components/Editor"
import Split from "react-split"
import { onSnapshot, addDoc, doc, deleteDoc, setDoc } from "firebase/firestore" //listen to changes in the firestore database and act accordingly in my local code eg: if send a delete request to database, onsnapshot will be running in background, and update local notes arr
import { notesCollection } from "./firebase"
import { db } from "./firebase"


export default function App() {

    const [notes, setNotes] = React.useState([]) //implicitly returns the value we have, this lazily initializes the state so it will only reach into the local storage the first time it loads andn so it doesnt reach into the note state on every single render 
    const [currentNoteId, setCurrentNoteId] = React.useState("") //ensure that notes at the index of 0 exists before we try and access the id of it. if notes[0] doesnt exist, then empty
    const [tempNoteText, setTempNoteText] = React.useState("")
    

    const currentNote = 
        notes.find(note => note.id ===currentNoteId
        )|| notes[0]

    const sortedNotes = notes.sort((a, b) => b.updatedAt - a.updatedAt);




    // React.useEffect(()=>{
    //     localStorage.setItem("notes", JSON.stringify(notes))
    // },[notes])//NOTE in order to interact with the localStorage everytime the notes array changes, want to set up side effect 
    
    React.useEffect(()=>{
        const unsubscribe = onSnapshot(notesCollection, function(snapshot){ //onsnapshot returns a fn tt we can save/ since using useEffect which has callback fn, if we return a fn, it should clean up any side effects
            const notesArr = snapshot.docs.map(doc => ({
                ...doc.data(), 
                id: doc.id//let firebase manage the id for each notes. doc.data doesmnt have it own id property so need this in addition

        }))
            setNotes(notesArr)
     }) //callback fn is to be executed whenever there is a change in the data, syncing up our local notes array w snapshot data. snapshot is the snapshot of the data at the time fn was called, and snapshot gets access to the most updated notes 
        return unsubscribe  
    }, []) //only want to set up onSnapshot event listener one time(when component first renders)
    //we are creating a websocket connection. therefore, need to give react a way to unsubscribe from this listener when component s unmounted(tab closed), causing mem leak

    React.useEffect(()=> {
        if(!currentNoteId){
            setCurrentNoteId(notes[0]?.id)
        }
        
    }, [notes])


    React.useEffect(()=>{
        if(currentNote){ 
            setTempNoteText(currentNote.body)
        }
    }, [currentNote]) 

    
    React.useEffect(()=>{
        const timeoutId = setTimeout(()=>{
            if(tempNoteText !== currentNote.body){
                updateNote(tempNoteText)
        }}, 500) 
        return () => clearTimeout(timeoutId)
    }, [tempNoteText])




    async function createNewNote() {
        const newNote = {
            body: "# Type your markdown note's title here",
            createdAt: Date.now(),
            updatedAt: Date.now()
        }
        const newNoteRef = await addDoc(notesCollection,newNote)
        setCurrentNoteId(newNoteRef.id)
    }
    
    async function updateNote(text) {
        const docRef = doc (db, "notes", currentNoteId)
       await setDoc(docRef, {body: text, updatedAt:Date.now()}, {merge:true})
    }

//  //note this is to put the most recently-modified note to the top
//  setNotes(oldNotes =>{ 
//     const newArray = []
//     for(let i = 0; i< oldNotes.length; i++) {
//         if (oldNotes[i].id ===currentNoteId){
//             newArray.unshift({...oldNotes[i], body:text})
//         }
//         else{
//             newArray.push(oldNotes[i])
//         }
        
//     }
//     return newArray
// })


    // oldNotes.map(oldNote => {
    //     return oldNote.id === currentNoteId
    //         ? { ...oldNote, body: text }
    //         : oldNote
    // })
    
      

    async function deleteNote(noteId) {
        const docRef = doc (db, "notes", noteId)
         await deleteDoc(docRef)
    }

    
    
    return (
        <main>
        {
            notes.length > 0 
            ?
             <Split 
                sizes={[30, 70]} 
                direction="horizontal" 
                  className="split"
            >
                <Sidebar
                    notes={sortedNotes}
                    currentNote={currentNote}//currentNote is a id of the node
                    setCurrentNoteId={setCurrentNoteId}//passes a function
                    newNote={createNewNote}//passes a function
                    deleteNote = {deleteNote}
                />
                
                    <Editor 
                        tempNoteText={tempNoteText} 
                        setTempNoteText={setTempNoteText} //passes a function
                    />
                
            </Split>
            :
            <div className="no-notes">
                <h1>You have no notes</h1>
                <button 
                    className="first-note" 
                    onClick={createNewNote}
                >
                    Create one now
                </button>
            </div>
            
        }
        </main>
    )
}
