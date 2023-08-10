import "./App.css";
import CreateFunction from "./pages/CreateFunction";
import EditFunction from "./pages/EditFunction";
import LandingPage from "./pages/LandingPage";
import { Routes, Route } from "react-router-dom";
import ListFunctions from "./pages/ListFunctions";
import SignUp from "./pages/SignUp";
import Login from "./pages/Login";
import { ToastContainer } from "react-toastify";
import PrivateRoute from "./hooks/auth/PrivateRoute";
import NotFound from "./pages/NotFound";
import TestTools from "./pages/TestTools";

function App() {
  return (
    <>
      <Routes>
        <Route exact path="/test" element={<TestTools />} />
        <Route exact path="/" element={<LandingPage />} />
        <Route
          exact
          path="/update/:id"
          element={
            <PrivateRoute>
              <EditFunction />
            </PrivateRoute>
          }
        />
        <Route
          exact
          path="/create"
          element={
            <PrivateRoute>
              <CreateFunction />
            </PrivateRoute>
          }
        />
        <Route
          exact
          path="/list"
          element={
            <PrivateRoute>
              <ListFunctions />
            </PrivateRoute>
          }
        />
        <Route
          exact
          path="/signup"
          element={
            <PrivateRoute secret={false}>
              <SignUp />
            </PrivateRoute>
          }
        />
        <Route
          exact
          path="/login"
          element={
            <PrivateRoute secret={false}>
              <Login />
            </PrivateRoute>
          }
        />
        <Route path="*" element={<NotFound />} />
      </Routes>
      <ToastContainer />
    </>
  );
}

export default App;
