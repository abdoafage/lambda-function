import React from "react";

function Modal({ setOpenModal, children }) {
  return (
    <>
      <div className="fixed inset-0 z-10 overflow-y-auto">
        <div
          className="fixed inset-0 w-full h-full bg-black opacity-40"
          onClick={() => setOpenModal(false)}
        ></div>
        <div className="flex items-center min-h-screen px-4 py-8">
          <div className="relative w-full max-w-lg p-4 mx-auto bg-white rounded-md shadow-lg">
            <div className="mt-3 sm:flex">
              <div className="mt-2 text-center sm:ml-4 sm:text-left">
                {children}
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Modal;
