import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { interviewApi } from '../services/interviewApi';

const Dashboard = ({ user }) => {
  const [interviews, setInterviews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const fetchInterviews = async () => {
      try {
        if (!user) return;
        const data = await interviewApi.getUserInterviews(user.id);
        setInterviews(data || []);
      } catch (err) {
        console.error(err);
        setError('Failed to load interviews. Using placeholder data.');
        // Set mock data in case backend isn't running yet so user can see something nice
        setInterviews([
          { id: 1, title: 'Java Backend Engineer Mock', status: 'COMPLETED', difficulty: 'MEDIUM', createdAt: '2026-08-19' },
          { id: 2, title: 'AI Developer Mock', status: 'ONGOING', difficulty: 'HARD', createdAt: '2026-08-20' },
        ]);
      } finally {
        setLoading(false);
      }
    };

    fetchInterviews();
  }, [user]);

  const handleStartNew = () => {
    navigate('/setup');
  };

  const handleResume = (id, status) => {
    if (status === 'COMPLETED') {
      navigate(`/result/${id}`);
    } else {
      navigate(`/interview/${id}`);
    }
  };

  return (
    <div className="container animate-fade-in" style={styles.container}>
      <header style={styles.header}>
        <div>
          <h1 style={{ margin: 0 }}>Welcome, {user?.username || 'Candidate'}!</h1>
          <p className="text-muted" style={{ margin: '0.3rem 0 0 0' }}>Manage your mock technical panels and analyze evaluations.</p>
        </div>
        <button className="btn-primary" onClick={handleStartNew}>
          + Setup New Interview
        </button>
      </header>

      {error && <div style={styles.warningAlert}>{error}</div>}

      <div style={styles.mainGrid}>
        <section style={styles.sessionSection} className="glass-panel">
          <h2 style={styles.sectionTitle}>Your Interviews</h2>
          {loading ? (
            <p>Loading sessions...</p>
          ) : interviews.length === 0 ? (
            <div style={styles.emptyState}>
              <p>You haven't taken any mock interviews yet.</p>
              <button className="btn-secondary" onClick={handleStartNew}>Start your first session</button>
            </div>
          ) : (
            <div style={styles.list}>
              {interviews.map((item) => (
                <div key={item.id} style={styles.listItem}>
                  <div>
                    <h4 style={{ margin: '0 0 0.3rem 0' }}>{item.title}</h4>
                    <div style={styles.metaRow}>
                      <span style={styles.metaLabel}>Difficulty:</span> {item.difficulty} | 
                      <span style={styles.metaLabel}> Created:</span> {new Date(item.createdAt).toLocaleDateString()}
                    </div>
                  </div>
                  <div style={styles.actionColumn}>
                    <span style={{
                      ...styles.statusBadge,
                      backgroundColor: item.status === 'COMPLETED' ? 'rgba(16, 185, 129, 0.15)' : 'rgba(245, 158, 11, 0.15)',
                      color: item.status === 'COMPLETED' ? '#10b981' : '#f59e0b',
                      borderColor: item.status === 'COMPLETED' ? '#10b981' : '#f59e0b',
                    }}>
                      {item.status}
                    </span>
                    <button className="btn-secondary" onClick={() => handleResume(item.id, item.status)}>
                      {item.status === 'COMPLETED' ? 'View Result' : 'Resume'}
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>

        <aside style={styles.statsPanel} className="glass-panel">
          <h3 style={styles.sectionTitle}>Performance Analytics</h3>
          <div style={styles.statBox}>
            <div style={styles.statNum}>8.2</div>
            <div style={styles.statLabel}>Average Score</div>
          </div>
          <div style={styles.statBox}>
            <div style={styles.statNum}>{interviews.filter(i => i.status === 'COMPLETED').length}</div>
            <div style={styles.statLabel}>Completed Interviews</div>
          </div>
          <div style={styles.statBox}>
            <div style={styles.statNum}>Java, SQL</div>
            <div style={styles.statLabel}>Top Rated Skills</div>
          </div>
        </aside>
      </div>
    </div>
  );
};

const styles = {
  container: {
    paddingTop: '3rem',
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '2.5rem',
  },
  mainGrid: {
    display: 'grid',
    gridTemplateColumns: '2fr 1fr',
    gap: '2rem',
  },
  sessionSection: {
    padding: '2rem',
  },
  sectionTitle: {
    fontSize: '1.25rem',
    marginBottom: '1.5rem',
    borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
    paddingBottom: '0.5rem',
  },
  list: {
    display: 'flex',
    flexDirection: 'column',
    gap: '1rem',
  },
  listItem: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '1rem 1.2rem',
    backgroundColor: 'rgba(255,255,255,0.02)',
    borderRadius: '8px',
    border: '1px solid rgba(255, 255, 255, 0.05)',
  },
  metaRow: {
    fontSize: '0.8rem',
    color: '#94a3b8',
  },
  metaLabel: {
    fontWeight: 'bold',
  },
  actionColumn: {
    display: 'flex',
    alignItems: 'center',
    gap: '1rem',
  },
  statusBadge: {
    fontSize: '0.75rem',
    padding: '2px 8px',
    borderRadius: '4px',
    border: '1px solid',
    fontWeight: 'bold',
  },
  statsPanel: {
    padding: '2rem',
    display: 'flex',
    flexDirection: 'column',
    gap: '1rem',
    height: 'fit-content',
  },
  statBox: {
    padding: '1rem',
    backgroundColor: 'rgba(255, 255, 255, 0.02)',
    borderRadius: '8px',
    textAlign: 'center',
    border: '1px solid rgba(255,255,255,0.04)',
  },
  statNum: {
    fontSize: '1.75rem',
    fontWeight: 'bold',
    color: '#38bdf8',
  },
  statLabel: {
    fontSize: '0.8rem',
    color: '#94a3b8',
    marginTop: '0.2rem',
  },
  emptyState: {
    textAlign: 'center',
    padding: '3rem 1rem',
    color: '#94a3b8',
  },
  warningAlert: {
    backgroundColor: 'rgba(245, 158, 11, 0.1)',
    border: '1px solid rgba(245, 158, 11, 0.2)',
    color: '#fbbf24',
    padding: '0.8rem',
    borderRadius: '8px',
    marginBottom: '1.5rem',
    fontSize: '0.9rem',
  }
};

export default Dashboard;
