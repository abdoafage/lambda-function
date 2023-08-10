import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import NavBar from "../components/NavBar";
import axois from "axios";
import { Loader } from "../components";
import useToken from "../hooks/auth/useToken";

function ListFunctions() {
  const [users, setUsers] = useState(null);
  const { token } = useToken();
  const getData = async () => {
    const { data } = await axois.get(`http://localhost:8000/functions/`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    });
    console.log(data);
    setUsers(data);
  };

  useEffect(() => {
    getData();
  }, []);

  return (
    <div className="bg-white">
      <NavBar />
      {!users ? (
        <div className="w-screen h-screen flex justify-center items-center">
          <Loader />
        </div>
      ) : (
        <div className=" m-5 p-3 shadow-lg shadow-[#b8b8b8]">
          <div className="flex justify-between items-center">
            <div className="">Functions ({users?.length})</div>
            <div className="flex">
              <button className="bg-white text-black border p-2 hover:bg-gray-100">
                <Link to="/create">Create</Link>
              </button>
            </div>
          </div>

          <div className="flex flex-col">
            <div className="sm:-mx-6 lg:-mx-8">
              <div className="inline-block w-screen py-2 sm:px-6 lg:px-8">
                <div className="">
                  <table className="border-collapse w-full text-left text-sm font-light">
                    <thead className="border-b font-medium dark:border-neutral-500">
                      <tr>
                        <th
                          scope="col"
                          className="px-6 py-2 border border-gray-200"
                        >
                          Function name
                        </th>
                        <th
                          scope="col"
                          className="px-6 py-2 border border-gray-200"
                        >
                          Description
                        </th>
                        <th
                          scope="col"
                          className="px-6 py-2 border border-gray-200"
                        >
                          Runtime
                        </th>
                        <th
                          scope="col"
                          className="px-6 py-2 border border-gray-200"
                        >
                          Last modified
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      {users &&
                        users.map((e) => (
                          <tr
                            key={e.id}
                            className="border dark:border-neutral-200"
                          >
                            <td className="whitespace-nowrap px-6 py-2 font-medium">
                              <Link
                                to={`/update/${e.id}`}
                                className="cursor-pointer underline text-blue-500"
                              >
                                {e.name}
                              </Link>
                            </td>
                            <td className="whitespace-normal px-6 py-2">
                              {e.description.substring(
                                0,
                                Math.min(e.description.length, 50)
                              )}
                              {e.description.length >= 50 ? "..." : ""}
                            </td>
                            <td className="whitespace-nowrap px-6 py-2">
                              {e.runtime}
                            </td>
                            <td className="whitespace-nowrap px-6 py-2">
                              {e.updated_at}
                            </td>
                          </tr>
                        ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default ListFunctions;
