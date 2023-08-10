import React from "react";

function Table() {
  return (
    <div className="flex flex-col">
      <div className="overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div className="inline-block min-w-full py-2 sm:px-6 lg:px-8">
          <div className="overflow-hidden">
            <table className="min-w-full text-left text-sm font-light">
              <thead className="border-b font-medium dark:border-neutral-500">
                <tr>
                  <th scope="col" className="px-6 py-4">
                    Function name
                  </th>
                  <th scope="col" className="px-6 py-4">
                    Description
                  </th>
                  <th scope="col" className="px-6 py-4">
                    Runtime
                  </th>
                  <th scope="col" className="px-6 py-4">
                    Last modified
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr className="border-b dark:border-neutral-500">
                  <td className="whitespace-nowrap px-6 py-4 font-medium">
                    firstFunc
                  </td>
                  <td className="whitespace-nowrap px-6 py-4">-</td>
                  <td className="whitespace-nowrap px-6 py-4">Python</td>
                  <td className="whitespace-nowrap px-6 py-4">2 days ago</td>
                </tr>
                <tr className="border-b dark:border-neutral-500">
                  <td className="whitespace-nowrap px-6 py-4 font-medium">2</td>
                  <td className="whitespace-nowrap px-6 py-4">Jacob</td>
                  <td className="whitespace-nowrap px-6 py-4">Thornton</td>
                  <td className="whitespace-nowrap px-6 py-4">@fat</td>
                </tr>
                <tr className="border-b dark:border-neutral-500">
                  <td className="whitespace-nowrap px-6 py-4 font-medium">3</td>
                  <td className="whitespace-nowrap px-6 py-4">Larry</td>
                  <td className="whitespace-nowrap px-6 py-4">Wild</td>
                  <td className="whitespace-nowrap px-6 py-4">@twitter</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

const Head = ({ children }) => {
  return (
    <thead className="border-b font-medium dark:border-neutral-500">
      {children}
    </thead>
  );
};
const Row = ({ children }) => {
  return <tr>{children}</tr>;
};

const TableCell = ({ children }) => {
  return (
    <th scope="col" className="px-6 py-4">
      {children}
    </th>
  );
};
export default Table;
