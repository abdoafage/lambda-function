import { useState } from "react";

function useToken() {
  const getToken = () => {
    const tokenString = sessionStorage.getItem("token");
    const userToken = JSON.parse(tokenString);
    return userToken;
  };

  const [token, setToken] = useState(getToken());

  const saveToken = (userToken) => {
    sessionStorage.setItem("token", JSON.stringify(userToken));
    console.log("userToken", userToken);
    setToken((prev) => userToken);
  };

  const removeToken = () => {
    sessionStorage.removeItem("token");
    setToken((prev) => null);
  };
  return {
    saveToken,
    token,
    removeToken,
  };
}

export default useToken;
