import React from "react";
import ReactDOM from "react-dom";
import ImageGen from "./ImageGen"
const App = () => {
  return (
    <div>
      <h1>Emoji Generater</h1>
      <ImageGen/>
    </div>
  );
};
export default App;
ReactDOM.render(<App />, document.getElementById("app"));
