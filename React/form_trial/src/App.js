import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes, Outlet, Link } from "react-router-dom"; // Import the new components
import ResultPage from "./ResultPage";
import YourRootComponent from "./YourRootComponent";

export default function App() {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    confirmPassword: "",
    okayToEmail: false,
  });

  const handleChange = (event) => {
    const { name, value, checked, type } = event.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  function handleSubmit(event) {
    event.preventDefault();
    const formMessages = [];
    if (formData.password === formData.confirmPassword) {
      formMessages.push("Successfully signed up");
    } else {
      formMessages.push("Passwords do not match");
    }
    if (formData.okayToEmail) {
      formMessages.push("Thanks for signing up for our newsletter!");
    }
    localStorage.setItem("formMessages", JSON.stringify(formMessages));
  }

  return (
    <Router>
      <div className="form-container">
        <form className="form" onSubmit={handleSubmit}>
          {/* Input fields and form elements */}
          <input
            type="email"
            placeholder="Email address"
            className="form--input"
            name="email"
            onChange={handleChange}
            value={formData.email}
          />
          <input
            type="password"
            placeholder="Password"
            className="form--input"
            name="password"
            onChange={handleChange}
            value={formData.password}
          />
          <input
            type="password"
            placeholder="Confirm password"
            className="form--input"
            name="confirmPassword"
            onChange={handleChange}
            value={formData.confirmPassword}
          />
          <div className="form--marketing">
            <input
              id="okayToEmail"
              type="checkbox"
              name="okayToEmail"
              onChange={handleChange}
              checked={formData.okayToEmail}
            />
            <label htmlFor="okayToEmail">I want to join the newsletter</label>
          </div>
          <button className="form--submit" type="submit">
            Sign up
          </button>
        </form>
      </div>

      <Routes>
      <Route path="/" element={<YourRootComponent />} />
        <Route path="/result" element={<ResultPage />} />
      </Routes>
    </Router>
  );
}
