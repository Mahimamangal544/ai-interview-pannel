import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { interviewApi } from '../services/interviewApi';

const Login = ({ onLoginSuccess }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [username, setUsername] = useState('');
  const [isRegister, setIsRegister] = useState(false);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      if (isRegister) {
        // Register API call mock/real
        const user = await interviewApi.register({ username, email, password });
        onLoginSuccess(user);
        navigate('/');
      } else {
        // Login API call mock/real
        const user = await interviewApi.login({ username: email, password }); // Username or email mapping
        onLoginSuccess(user);
        navigate('/');
      }
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.message || 'Authentication failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card} className="glass-panel animate-fade-in">
        <h2 style={styles.title}>{isRegister ? 'Create Account' : 'Welcome Back'}</h2>
        <p style={styles.subtitle}>
          {isRegister ? 'Register to start your mock interviews' : 'Login to manage your panel sessions'}
        </p>

        {error && <div style={styles.error}>{error}</div>}

        <form onSubmit={handleSubmit} style={styles.form}>
          {isRegister && (
            <div style={styles.inputGroup}>
              <label style={styles.label}>Username</label>
              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Choose a username"
                required
              />
            </div>
          )}

          <div style={styles.inputGroup}>
            <label style={styles.label}>{isRegister ? 'Email Address' : 'Username / Email'}</label>
            <input
              type={isRegister ? 'email' : 'text'}
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder={isRegister ? 'Enter email address' : 'Enter username or email'}
              required
            />
          </div>

          <div style={styles.inputGroup}>
            <label style={styles.label}>Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="••••••••"
              required
            />
          </div>

          <button type="submit" className="btn-primary" style={styles.button} disabled={loading}>
            {loading ? 'Processing...' : isRegister ? 'Register' : 'Sign In'}
          </button>
        </form>

        <div style={styles.toggleText}>
          {isRegister ? 'Already have an account?' : "Don't have an account?"}{' '}
          <span style={styles.toggleLink} onClick={() => setIsRegister(!isRegister)}>
            {isRegister ? 'Sign In' : 'Create one'}
          </span>
        </div>
      </div>
    </div>
  );
};

const styles = {
  container: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    flex: 1,
    padding: '2rem',
  },
  card: {
    width: '100%',
    maxWidth: '420px',
    padding: '2.5rem 2rem',
  },
  title: {
    fontSize: '1.75rem',
    fontWeight: '700',
    textAlign: 'center',
    marginBottom: '0.5rem',
  },
  subtitle: {
    color: '#94a3b8',
    textAlign: 'center',
    marginBottom: '2rem',
    fontSize: '0.9rem',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    gap: '1.2rem',
  },
  inputGroup: {
    display: 'flex',
    flexDirection: 'column',
    gap: '0.4rem',
  },
  label: {
    fontSize: '0.85rem',
    fontWeight: '500',
    color: '#cbd5e1',
  },
  button: {
    marginTop: '0.8rem',
    padding: '0.9rem',
  },
  error: {
    backgroundColor: 'rgba(239, 68, 68, 0.1)',
    border: '1px solid rgba(239, 68, 68, 0.2)',
    color: '#f87171',
    padding: '0.8rem',
    borderRadius: '6px',
    marginBottom: '1.2rem',
    fontSize: '0.9rem',
    textAlign: 'center',
  },
  toggleText: {
    textAlign: 'center',
    marginTop: '1.5rem',
    fontSize: '0.875rem',
    color: '#94a3b8',
  },
  toggleLink: {
    color: '#38bdf8',
    cursor: 'pointer',
    fontWeight: '600',
  },
};

export default Login;
