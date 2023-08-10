import React from "react";
import useToken from "./useToken";
import { Navigate, Route } from "react-router-dom";

function PrivateRoute({ secret = true, children }) {
  const { token } = useToken();
  //   console.log(token);
  const tokenBool = Boolean(token);
  //   console.log(tokenBool);
  const pass = secret ^ tokenBool;
  //   console.log(!pass);
  if (!pass) return children;
  else return <Navigate to={secret ? "/login" : "/create"} replace />;
}

export default PrivateRoute;
