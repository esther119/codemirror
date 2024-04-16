import React from "react";
import ReactDOM from "react-dom";
import PythonEditor from "./PythonEditor"; // Adjust the import path as necessary

export default function App() {
  return (
    <div className="App">
      <h1>Hello</h1>
      <PythonEditor />
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
