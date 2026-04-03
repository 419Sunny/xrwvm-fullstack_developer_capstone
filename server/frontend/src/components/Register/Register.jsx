import React, { useState } from 'react';
import './Register.css';
import Header from '../Header/Header';

const Register = () => {
  const [username, setUsername] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch(window.location.origin + '/djangoapp/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        userName: username,
        first_name: firstName,
        last_name: lastName,
        email,
        password,
      }),
    });
    const data = await response.json();
    if (data.status === 'Success') {
      window.location.href = '/login';
    } else {
      alert(data.message || 'Registration failed.');
    }
  };

  return (
    <div>
      <Header />
      <div className='register_container'>
        <h1>Register</h1>
        <form onSubmit={handleSubmit} className='register_form'>
          <label>Username</label>
          <input type='text' value={username} onChange={(e) => setUsername(e.target.value)} required />
          <label>First Name</label>
          <input type='text' value={firstName} onChange={(e) => setFirstName(e.target.value)} required />
          <label>Last Name</label>
          <input type='text' value={lastName} onChange={(e) => setLastName(e.target.value)} required />
          <label>Email</label>
          <input type='email' value={email} onChange={(e) => setEmail(e.target.value)} required />
          <label>Password</label>
          <input type='password' value={password} onChange={(e) => setPassword(e.target.value)} required />
          <button type='submit'>Register</button>
        </form>
      </div>
    </div>
  );
};

export default Register;
