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
          <label htmlFor='register-username'>Username</label>
          <input
            id='register-username'
            type='text'
            placeholder='Username'
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <label htmlFor='register-firstname'>First Name</label>
          <input
            id='register-firstname'
            type='text'
            placeholder='First Name'
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            required
          />
          <label htmlFor='register-lastname'>Last Name</label>
          <input
            id='register-lastname'
            type='text'
            placeholder='Last Name'
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            required
          />
          <label htmlFor='register-email'>Email</label>
          <input
            id='register-email'
            type='email'
            placeholder='Email'
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <label htmlFor='register-password'>Password</label>
          <input
            id='register-password'
            type='password'
            placeholder='Password'
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button type='submit'>Register</button>
        </form>
      </div>
    </div>
  );
};

export default Register;
