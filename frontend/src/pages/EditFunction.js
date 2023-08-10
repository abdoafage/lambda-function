import { useEffect, useState } from "react";
import AceEditor from "react-ace";
import "ace-builds/src-noconflict/mode-python";
import "ace-builds/src-noconflict/mode-javascript";
import "ace-builds/src-noconflict/mode-json5";
import "ace-builds/src-noconflict/ext-language_tools";
import "ace-builds/src-noconflict/theme-cobalt";
import "ace-builds/src-noconflict/theme-tomorrow";
import { Button, Input } from "../components";
import { useParams } from "react-router-dom";
import "../App.css";
import NavBar from "../components/NavBar";
import axios from "axios";
import useToken from "../hooks/auth/useToken";
import Modal from "../components/Modal";

const runtimeToLang = {
  Python: "python",
  Node: "javascript",
};

function EditFunction() {
  const { id } = useParams();
  const { token } = useToken();

  const [functionData, setFunctionData] = useState({});
  const [resultOfFunctionTest, setResultOfFunctionTest] = useState({});
  const [lang1, setLang1] = useState("python");
  const [lang2, setLang2] = useState("json5");

  const [code1, setCode1] = useState("");
  const [code2, setCode2] = useState(`{
    "item1": "item1",
    "item2": "item2",
    "item3": "item3"
}`);

  const [showModal, setShowModal] = useState(false);
  const [showModalRun, setShowModalRun] = useState(false);
  const getData = async () => {
    try {
      const { data } = await axios.get(
        `http://localhost:8000/functions/${id}/`,
        {
          headers: {
            Authorization: `Token ${token}`,
          },
        }
      );
      // console.log(data);
      setCode1((prev) => data.body);
      setLang1((prev) => runtimeToLang[data.runtime]);
      setFunctionData((prev) => data);
    } catch (error) {
      console.log(error);
    }
  };
  useEffect(() => {
    getData();
  }, []);

  function onChange1(newValue) {
    console.log("change", newValue);
    setCode1(newValue);
  }

  function onChange2(newValue) {
    console.log("change", newValue);
    setCode2(newValue);
  }

  function HandleTest() {
    console.log("HandleTest");
    console.log(JSON.parse(code2));
    axios
      .post(`http://localhost:8000/functions/test/${id}/`, JSON.parse(code2), {
        headers: {
          Authorization: `Token ${token}`,
        },
      })
      .then((res) => res.data)
      .then((data) => {
        console.log(data);
        // setCode3((prev) => data.message);
        setResultOfFunctionTest((prev) => data);
        setShowModal(true);
      });
  }
  function HandleRun() {
    console.log("HandleRun");
    setShowModalRun(true);
  }
  function HandleDeploy() {
    console.log("HandleDeploy");
    axios
      .patch(
        `http://localhost:8000/functions/update/${id}/`,
        {
          body: code1.trim(),
        },
        {
          headers: {
            Authorization: `Token ${token}`,
          },
        }
      )
      .then((res) => {
        setFunctionData((prev) => ({ ...prev, body: code1.trim() }));
        setCode1((prev) => prev.trim());
        console.log(res.data);
        return res.data;
      })
      .catch((err) => console.log(err));
  }

  return (
    <>
      <NavBar />
      <div className="App">
        <div className="AceEditor">
          <div className="shadow-md my-1">
            <div className="bg-blue-100 border  p-2 font-bold text-xl">
              Code properties:
            </div>

            <ul className="p-2 flex justify-between">
              <li className="flex-1">
                <div className="text-gray-600">Package size: </div>{" "}
                <div className="text-sm">
                  {new TextEncoder().encode(functionData.body).length} bytes
                </div>
              </li>
              <li className="flex-1">
                <div className="text-gray-600">ID: </div>{" "}
                <div className="text-sm">{id}</div>
              </li>
              <li className="flex-1">
                <div className="text-gray-600">Last Updated: </div>{" "}
                <div className="text-sm">{functionData.updated_at}</div>
              </li>
              <li className="flex-1">
                <div className="text-gray-600">Runtime: </div>{" "}
                <div className="text-sm">{functionData.runtime}</div>
              </li>
            </ul>
          </div>
          <div className="Editor_controller shadow-md my-3">
            <button
              className="bg-white text-black border p-2 hover:bg-gray-100"
              onClick={HandleTest}
            >
              Test
            </button>
            {showModal && (
              <Modal setOpenModal={setShowModal}>
                <h3 className="text-lg font-bold text-gray-800">Results:</h3>
                <p className="mt-2 font-bold text-[15px] leading-relaxed text-gray-500">
                  Status:{" "}
                  <span
                    className={
                      resultOfFunctionTest.status
                        ? "text-green-700"
                        : "text-red-700"
                    }
                  >
                    {resultOfFunctionTest.status ? "OK" : "FAILED"}
                  </span>
                </p>
                <p className="mt-2 font-bold text-[15px] leading-relaxed text-gray-500">
                  Time execution: {resultOfFunctionTest.execution_time} s
                </p>
                <p className="mt-2 font-bold text-[15px] leading-relaxed text-gray-500">
                  {resultOfFunctionTest.status ? "Output" : "Error message"}:{" "}
                  {resultOfFunctionTest.message}
                </p>
              </Modal>
            )}
            <button
              className="bg-white text-black border p-2 hover:bg-gray-100"
              onClick={HandleRun}
            >
              Run
            </button>
            {showModalRun && (
              <Modal setOpenModal={setShowModalRun}>
                <h3 className="text-lg font-bold text-gray-800">
                  Your function link:
                </h3>
                <p className="mt-2 font-bold text-[15px] leading-relaxed text-gray-500">
                  Link: http://localhost:8000/run/{id}/
                </p>
              </Modal>
            )}
            <button
              className="disabled:text-gray-300 disabled:bg-white disabled:cursor-not-allowed bg-white text-black border p-2 hover:bg-gray-100"
              onClick={HandleDeploy}
              disabled={code1 === functionData.body}
            >
              Deploy
            </button>
          </div>
          <div className="Editor_screens border shadow-md my-3">
            <div className="CodeSection border  m-1 p-1 shadow-md">
              <div>Function:</div>

              <AceEditor
                className="screen_1"
                mode={lang1}
                theme="cobalt"
                value={code1}
                onChange={onChange1}
                width="auto"
                height="100%"
                name="PYTHON_EDITOR"
                editorProps={{ $blockScrolling: true }}
                setOptions={{
                  enableBasicAutocompletion: true,
                  enableLiveAutocompletion: true,
                  showPrintMargin: false,
                }}
              />
            </div>
            <div className="JsonSection border shadow-md m-1 p-1">
              <div>Params ( JSON ):</div>
              <AceEditor
                className="screen_2"
                mode={lang2}
                theme="tomorrow"
                value={code2}
                onChange={onChange2}
                width="auto"
                height="100%"
                name="JSON_EDITOR"
                editorProps={{ $blockScrolling: true }}
                setOptions={{
                  enableBasicAutocompletion: true,
                  enableLiveAutocompletion: true,
                  enableSnippets: true,
                  tabSize: 2,
                }}
              />
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default EditFunction;
