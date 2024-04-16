import React from "react";
import { EditorView } from "@uiw/react-codemirror";
import { python } from "@codemirror/lang-python";

function PythonEditor() {
  const [code, setCode] = React.useState("# Write your Python code here\n");

  return (
    <EditorView
      value={code}
      height="200px"
      extensions={[python()]}
      onChange={(value, viewUpdate) => {
        setCode(value);
      }}
    />
  );
}

export default PythonEditor;
