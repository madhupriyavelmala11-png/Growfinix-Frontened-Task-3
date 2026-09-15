import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
// Removed index.css import to avoid conflicts with our App.css

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
