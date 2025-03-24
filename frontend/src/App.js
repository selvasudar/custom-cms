import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Login from './components/Login';
import Signup from './components/Signup';
import CreatePost from './components/CreatePost';

function ProtectedRoute({ children }) {
  return localStorage.getItem('token') ? children : <Navigate to="/" />;
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route
          path="/create-post"
          element={<ProtectedRoute><CreatePost /></ProtectedRoute>}
        />
      </Routes>
    </Router>
  );
}

export default App;