import React, { useState } from "react";
import { Link } from "react-router-dom";
import NavBar from "../components/NavBar";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import useToken from "../hooks/auth/useToken";

const CreateFunction = () => {
  const navigate = useNavigate();
  const { token } = useToken();

  const [form, setForm] = useState({
    name: "",
    Runtime: "Python",
    description: "",
  });

  const HandleFunctionName = (e) => {
    setForm({ ...form, name: e.target.value });
  };

  const HandleRuntimeChange = (e) => {
    console.log(e.target.value);
    setForm({ ...form, Runtime: e.target.value });
  };

  const HandleDescriptionChange = (e) => {
    console.log(e.target.value);
    setForm({ ...form, description: e.target.value });
  };

  const GetData = async () => {
    try {
      const { data } = await axios.post(
        `http://localhost:8000/functions/create/`,
        {
          name: form.name,
          body: "def example():\n    print('Hello world !!!')",
        },
        {
          headers: {
            Authorization: `Token ${token}`,
          },
        }
      );
      // console.log(data);
      navigate(`/update/${data.id}`);
    } catch (err) {
      console.log(err);
    }
  };

  const HandleSubmit = (e) => {
    e.preventDefault();
    console.log(form);
    // navigate("/update/3");
    GetData();
  };

  return (
    <>
      <NavBar />
      <div className="min-h-screen p-6 bg-gray-100 flex items-center justify-center">
        <div className="bg-white w-[700px] rounded shadow-lg p-4 px-4 md:p-8 mb-6">
          <div className="flex text-sm ">
            <div className="flex-1 text-gray-600">
              <p className="text-xl font-bold">Information Form: </p>
              <p className="text-[10px]">
                This form is designed to gather essential details about a
                function, ensuring a comprehensive understanding of its purpose
                and usage.{" "}
              </p>
            </div>

            <div className="flex-2">
              <form onSubmit={HandleSubmit}>
                <div className="text-sm ">
                  <div className="md:col-span-5">
                    <label htmlFor="function_name">Function name *</label>
                    <input
                      type="text"
                      name="function_name"
                      id="function_name"
                      className="h-10 border mt-1 rounded px-4 w-full bg-gray-50"
                      placeholder="myFunctionName"
                      onChange={HandleFunctionName}
                    />
                  </div>

                  <div className="sm:col-span-5 mt-3">
                    <label
                      htmlFor="Runtime"
                      className="block text-sm font-medium leading-6 text-gray-900"
                    >
                      Runtime *
                    </label>
                    <div className="mt-1">
                      <select
                        id="Runtime"
                        name="Runtime"
                        autoComplete="Runtime-name"
                        className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6"
                        onChange={HandleRuntimeChange}
                      >
                        <option value="Python">Python</option>
                        <option value="Nodejs">Node</option>
                      </select>
                    </div>
                  </div>

                  <div className="col-span-full mt-3">
                    <label
                      htmlFor="about"
                      className="block text-sm font-medium leading-6 text-gray-900"
                    >
                      description
                    </label>
                    <div className="mt-1">
                      <textarea
                        id="description"
                        name="description"
                        rows="3"
                        className="block w-full rounded-md border-0 p-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                        onChange={HandleDescriptionChange}
                      ></textarea>
                    </div>
                    <p className="mt-3 text-[10px] leading-6 text-gray-600">
                      In this section, please provide a detailed description of
                      <br />
                      the function's functionality and objective.
                    </p>
                  </div>

                  <div className="md:col-span-5 text-right">
                    <div className="inline-flex items-end">
                      <button
                        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                        // onClick={HandleSubmit}
                        type="submit"
                      >
                        Create
                      </button>
                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
export default CreateFunction;
