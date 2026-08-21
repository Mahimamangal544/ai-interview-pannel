import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { interviewApi } from '../services/interviewApi';

const InterviewSetup = ({ user }) => {
  const [title, setTitle] = useState('');
  const [difficulty, setDifficulty] = useState('MEDIUM');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleStart = async (e) => {
    e.preventDefault();
    if (!title.trim()) return;

    setLoading(true);
    setError('');

    try {
      const payload = {
        userId: user?.id || 1, // Fallback if no logged in user context
        title: title,
        difficulty: difficulty
      };
      
      const newInterview = await interviewApi.createInterview(payload);
      navigate(`/interview/${newInterview.id}`);
    } catch (err) {
      console.error(err);
      setError('Failed to setup interview session. Redirecting to mock session...');
      setTimeout(() => {
        navigate('/interview/mock-123');
      }, 1500);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container animate-fade-in" style={styles.container}>
      <div style={styles.card} className="glass-panel">
        <h2 style={styles.title}>Interview Setup Panel</h2>
        <p className="text-muted" style={styles.subtitle}>
          Configure your technical area, topics, and initial difficulty levels.
        </p>

        {error && <div style={styles.error}>{error}</div>}

        <form onSubmit={handleStart} style={styles.form}>
          <div style={styles.inputGroup}>
            <label style={styles.label}>Interview Title / Goal</label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="e.g. Java Spring Boot Developer Interview"
              required
            />
          </div>

          <div style={styles.inputGroup}>
            <label style={styles.label}>Target Difficulties</label>
            <select 
              value={difficulty} 
              onChange={(e) => setDifficulty(e.target.value)}
              style={styles.select}
            >
              <option value="EASY">Easy (Conceptual review)</option>
              <option value="MEDIUM">Medium (Core developer level)</option>
              <option value="HARD">Hard (Architect / Deep dive)</option>
            </select>
          </div>

          <div style={styles.note}>
            <strong>Note:</strong> The panel uses adaptive routing. The difficulty will automatically scale dynamically depending on the depth of your answers!
          </div>

          <div style={styles.buttonGroup}>
            <button 
              type="button" 
              className="btn-secondary"
              onClick={() => navigate('/')}
              disabled={loading}
            >
              Back to Dashboard
            </button>
            <button 
              type="submit" 
              className="btn-primary"
              disabled={loading || !title.trim()}
            >
              {loading ? 'Creating session...' : 'Launch AI Panel'}
            </button>
          </div>
        </form>
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
  },
  card: {
    width: '100%',
    maxWidth: '550px',
    padding: '2.5rem',
  },
  title: {
    fontSize: '1.75rem',
    fontWeight: '700',
    marginBottom: '0.5rem',
    textAlign: 'center',
  },
  subtitle: {
    fontSize: '0.9rem',
    marginBottom: '2rem',
    textAlign: 'center',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    gap: '1.5rem',
  },
  inputGroup: {
    display: 'flex',
    flexDirection: 'column',
    gap: '0.5rem',
  },
  label: {
    fontSize: '0.85rem',
    fontWeight: '600',
    color: '#cbd5e1',
  },
  select: {
    cursor: 'pointer',
  },
  note: {
    padding: '0.8rem 1rem',
    backgroundColor: 'rgba(56, 189, 248, 0.05)',
    border: '1px solid rgba(56, 189, 248, 0.15)',
    borderRadius: '8px',
    fontSize: '0.85rem',
    lineHeight: '1.4',
    color: '#cbd5e1',
  },
  buttonGroup: {
    display: 'flex',
    justifyContent: 'space-between',
    gap: '1rem',
    marginTop: '0.5rem',
  },
  error: {
    backgroundColor: 'rgba(245, 158, 11, 0.1)',
    border: '1px solid rgba(245, 158, 11, 0.2)',
    color: '#fbbf24',
    padding: '0.8rem',
    borderRadius: '6px',
    marginBottom: '1.2rem',
    fontSize: '0.85rem',
    textAlign: 'center',
  }
};

export default InterviewSetup;
