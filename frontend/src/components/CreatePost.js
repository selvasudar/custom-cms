import { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import '../styles.css'; // Optional: apply similar styling if desired

function CreatePost() {
  const [formData, setFormData] = useState({
    title: '', description: '', content: '', featureImage: null, thumbnail: null
  });
  const navigate = useNavigate();

  useEffect(() => {
    // Check if user is logged in
    if (!localStorage.getItem('token')) {
      navigate('/');
    }
  }, [navigate]);

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    setFormData({ ...formData, [name]: files ? files[0] : value });
  };

  const handleSubmit = async () => {
    console.log("localStorage.getItem('token') ",localStorage.getItem('token') )
    const data = new FormData();
    data.append('title', formData.title);
    data.append('description', formData.description);
    data.append('content', formData.content);
    data.append('feature_image', formData.featureImage);
    data.append('thumbnail', formData.thumbnail);
    data.append('user_id', localStorage.getItem('user_id'));

    try {
      const res = await axios.post('http://127.0.0.1:5000/api/posts', data, {
        headers: { 'Authorization': localStorage.getItem('token') }
      });
      alert('Post created!');
    } catch (err) {
      alert('Failed to create post: ' + (err.response?.data?.message || 'Unknown error'));
      if (err.response?.status === 401) navigate('/'); // Redirect to login if unauthorized
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <h1>Create Post</h1>
        <input className="auth-input" name="title" onChange={handleChange} placeholder="Title" />
        <textarea className="auth-input" name="description" onChange={handleChange} placeholder="Description" />
        <textarea className="auth-input" name="content" onChange={handleChange} placeholder="Content" />
        <input className="auth-input" type="file" name="featureImage" onChange={handleChange} />
        <input className="auth-input" type="file" name="thumbnail" onChange={handleChange} />
        <button className="auth-button" onClick={handleSubmit}>Submit</button>
      </div>
    </div>
  );
}

export default CreatePost;