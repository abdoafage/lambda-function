import React, { useState } from "react";
import Modal from "../components/Modal";
import Dropdown from "../components/Dropdown";
import { Link } from "react-router-dom";

function TestTools() {
  const [showModal, setShowModal] = useState(false);
  const HandleFocus = (e) => {
    console.log(e);
  };
  return (
    <>
      {/* // <div className="flex flex-col items-center justify-center h-60">
    //   <h1 className="text-2xl font-bold">
    //     Click on the button to open the modal.
    //   </h1>
    //   <button
    //     className="px-4 py-2 text-purple-100 bg-purple-600 rounded-md"
    //     type="button"
    //     onClick={() => {
    //       setShowModal(true);
    //     }}
    //   >
    //     Open Modal
    //   </button>

    //   {showModal && <Modal setOpenModal={setShowModal} />}
    // </div> */}
      <Dropdown button={<Link to={"#"}>welcome</Link>}>
        <div>woooo</div>
      </Dropdown>
    </>
  );
}

export default TestTools;
