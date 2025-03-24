import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import '../styles.css'; // Import the CSS

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const res = await axios.post('http://127.0.0.1:5000/api/login', { username, password });
      if (res.status === 200) {
        localStorage.setItem('user_id', res.data.user_id);
        localStorage.setItem('token', res.data.token); // Store the token
        navigate('/create-post');
      }
    } catch (err) {
      setError(err.response?.data?.message || 'Login failed');
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <h1>Login</h1>
        {error && <p className="error-message">{error}</p>}
        <input
          className="auth-input"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Username"
        />
        <input
          className="auth-input"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
        />
        <button className="auth-button" onClick={handleLogin}>
          Login
        </button>
        <div className="auth-link">
          <a href="/signup">Need an account? Signup</a>
        </div>
      </div>
    </div>
  );
}

export default Login;