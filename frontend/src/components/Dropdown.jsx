import React, { useState } from "react";

function Dropdown({ button, children }) {
  const [dropHit, setDropHit] = useState(false);
  return (
    <>
      <div className="relative inline-block text-left">
        <div>
          <button
            type="button"
            className="inline-flex w-full justify-center gap-x-1.5 rounded-md px-3 py-2 text-sm font-semibold"
            id="menu-button"
            aria-expanded="true"
            aria-haspopup="true"
            onClick={() => setDropHit((prev) => !prev)}
          >
            {button}
          </button>
        </div>

        <div
          className={`absolute ${
            dropHit ? "" : "hidden"
          } right-0 z-10 mt-2 w-full origin-top-right divide-y divide-gray-100 rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none`}
          role="menu"
          aria-orientation="vertical"
          aria-labelledby="menu-button"
          tabIndex="-1"
        >
          {children}
        </div>
      </div>
    </>
  );
}

export default Dropdown;
