import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate, Link } from 'react-router-dom';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import InterviewSetup from './pages/InterviewSetup';
import Interview from './pages/Interview';
import Result from './pages/Result';

function App() {
  const [user, setUser] = useState(null);
  const [initialized, setInitialized] = useState(false);

  useEffect(() => {
    // Check if user is cached locally
    const cachedUser = localStorage.getItem('currentUser');
    if (cachedUser) {
      try {
        setUser(JSON.parse(cachedUser));
      } catch (e) {
        console.error(e);
      }
    }
    setInitialized(true);
  }, []);

  const handleLoginSuccess = (userData) => {
    setUser(userData);
    localStorage.setItem('currentUser', JSON.stringify(userData));
  };

  const handleLogout = () => {
    setUser(null);
    localStorage.removeItem('currentUser');
  };

  if (!initialized) {
    return <div style={{ color: '#fff', textAlign: 'center', marginTop: '5rem' }}>Loading panel settings...</div>;
  }

  return (
    <Router>
      {user && (
        <nav className="navbar">
          <div className="brand">
            <span>🤖</span> Coordinated AI Interview Panel
          </div>
          <div className="nav-links">
            <Link to="/">Dashboard</Link>
            <Link to="/setup">New Interview</Link>
            <a href="#logout" onClick={handleLogout} style={{ color: '#f87171' }}>
              Logout
            </a>
          </div>
        </nav>
      )}

      <Routes>
        <Route 
          path="/login" 
          element={!user ? <Login onLoginSuccess={handleLoginSuccess} /> : <Navigate to="/" />} 
        />
        
        <Route 
          path="/" 
          element={user ? <Dashboard user={user} /> : <Navigate to="/login" />} 
        />
        
        <Route 
          path="/setup" 
          element={user ? <InterviewSetup user={user} /> : <Navigate to="/login" />} 
        />
        
        <Route 
          path="/interview/:id" 
          element={user ? <Interview /> : <Navigate to="/login" />} 
        />
        
        <Route 
          path="/result/:id" 
          element={user ? <Result /> : <Navigate to="/login" />} 
        />

        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </Router>
  );
}

export default App;
