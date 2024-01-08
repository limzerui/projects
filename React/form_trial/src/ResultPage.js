// ResultPage.js
import React from "react";
import { Link } from "react-router-dom";

function ResultPage() {
  // Retrieve the messages from local storage or another data source
  const messages = JSON.parse(localStorage.getItem("formMessages"));

  return (
    <div>
      <h1>Form Submission Result</h1>
      <div>
        {messages.map((message, index) => (
          <p key={index}>{message}</p>
        ))}
      </div>
      <Link to="/">Go back to the form</Link>
    </div>
  );
}

export default ResultPage;
