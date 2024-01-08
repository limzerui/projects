import { initializeApp } from "firebase/app";
import { getFirestore, collection } from "firebase/firestore"

const firebaseConfig = {
  apiKey: "AIzaSyDmCDMfphWM9dMSb6fs-qWb_KTK_dRm6Nw",
  authDomain: "react-notes-fa9dc.firebaseapp.com",
  projectId: "react-notes-fa9dc",
  storageBucket: "react-notes-fa9dc.appspot.com",
  messagingSenderId: "486925688500",
  appId: "1:486925688500:web:aaaec81688cff822fcc1e1"
};

const app = initializeApp(firebaseConfig);
export const db = getFirestore(app)
export const notesCollection = collection(db, "notes")
