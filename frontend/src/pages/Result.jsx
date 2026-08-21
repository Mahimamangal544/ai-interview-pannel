import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { interviewApi } from '../services/interviewApi';

const Result = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchResult = async () => {
      try {
        const data = await interviewApi.getInterviewResult(id);
        setResult(data);
      } catch (err) {
        console.error(err);
        setError('Could not retrieve results from server. Using local mock report.');
        // Set beautiful local mock report
        setResult({
          overallScore: 7.8,
          summary: 'The candidate demonstrated a strong grasp of OOP fundamentals and database management. They expressed clean conceptual understanding of Java class relations. However, their Spring Boot configuration knowledge was moderate, and they failed to fully optimize complex data structure complexities.',
          recommendations: 'Focus on practicing time-complexity proofs, dynamic programming, and study Spring Boot bean lifecycles.',
          skillsBreakdown: [
            { skill: 'Java', score: 8.5 },
            { skill: 'MySQL', score: 8.0 },
            { skill: 'Spring Boot', score: 7.0 },
            { skill: 'Data Structures', score: 6.5 },
            { skill: 'Python', score: 9.0 }
          ]
        });
      } finally {
        setLoading(false);
      }
    };

    fetchResult();
  }, [id]);

  if (loading) {
    return <div className="container" style={styles.loading}>Generating report...</div>;
  }

  return (
    <div className="container animate-fade-in" style={styles.container}>
      <div style={styles.card} className="glass-panel">
        <h1 style={styles.title}>Interview Performance Report</h1>
        <p className="text-muted text-center" style={{ marginBottom: '2.5rem' }}>
          Session ID: {id}
        </p>

        {error && <div style={styles.alert}>{error}</div>}

        <div style={styles.scoreSection}>
          <div style={styles.gauge}>
            <span style={styles.scoreText}>{result?.overallScore?.toFixed(1) || '0.0'}</span>
            <span style={styles.gaugeLabel}>Overall Grade</span>
          </div>
        </div>

        <div style={styles.reportSection}>
          <h3>Evaluation Summary</h3>
          <p style={styles.text}>{result?.summary}</p>
        </div>

        <div style={styles.reportSection}>
          <h3>Recommendations</h3>
          <p style={{ ...styles.text, color: '#fbbf24' }}>{result?.recommendations}</p>
        </div>

        <div style={styles.skillsSection}>
          <h3>Skill Performance Breakdown</h3>
          <div style={styles.skillsList}>
            {result?.skillsBreakdown?.map((item, index) => (
              <div key={index} style={styles.skillRow}>
                <span style={styles.skillName}>{item.skill}</span>
                <div style={styles.skillBarTrack}>
                  <div 
                    style={{ 
                      ...styles.skillBarFill, 
                      width: `${item.score * 10}%`,
                      backgroundColor: item.score >= 7.5 ? '#10b981' : item.score >= 5.0 ? '#f59e0b' : '#ef4444'
                    }} 
                  />
                </div>
                <span style={styles.skillScore}>{item.score.toFixed(1)}/10</span>
              </div>
            ))}
          </div>
        </div>

        <div style={styles.buttonGroup}>
          <button className="btn-primary" onClick={() => navigate('/')} style={styles.backButton}>
            Return to Dashboard
          </button>
        </div>
      </div>
    </div>
  );
};

const styles = {
  container: {
    paddingTop: '3rem',
    display: 'flex',
    justifyContent: 'center',
  },
  card: {
    width: '100%',
    maxWidth: '750px',
    padding: '3rem 2.5rem',
  },
  title: {
    textAlign: 'center',
    fontSize: '2rem',
    marginBottom: '0.5rem',
  },
  scoreSection: {
    display: 'flex',
    justifyContent: 'center',
    margin: '2rem 0',
  },
  gauge: {
    width: '150px',
    height: '150px',
    borderRadius: '50%',
    border: '4px solid #38bdf8',
    boxShadow: '0 0 20px rgba(56, 189, 248, 0.2)',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(56, 189, 248, 0.05)',
  },
  scoreText: {
    fontSize: '3rem',
    fontWeight: '800',
    color: '#38bdf8',
    lineHeight: '1',
  },
  gaugeLabel: {
    fontSize: '0.8rem',
    color: '#cbd5e1',
    marginTop: '0.2rem',
  },
  reportSection: {
    marginBottom: '2rem',
    padding: '1.2rem 1.5rem',
    backgroundColor: 'rgba(255, 255, 255, 0.02)',
    borderRadius: '8px',
    border: '1px solid rgba(255,255,255,0.05)',
  },
  text: {
    lineHeight: '1.6',
    color: '#cbd5e1',
    margin: '0.5rem 0 0 0',
  },
  skillsSection: {
    marginBottom: '2.5rem',
  },
  skillsList: {
    display: 'flex',
    flexDirection: 'column',
    gap: '1rem',
    marginTop: '1rem',
  },
  skillRow: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    gap: '1.5rem',
  },
  skillName: {
    fontSize: '0.95rem',
    fontWeight: '600',
    width: '140px',
  },
  skillBarTrack: {
    flex: 1,
    height: '10px',
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: '5px',
    overflow: 'hidden',
  },
  skillBarFill: {
    height: '100%',
    borderRadius: '5px',
    transition: 'width 1s ease-out',
  },
  skillScore: {
    fontSize: '0.9rem',
    fontWeight: 'bold',
    width: '60px',
    textAlign: 'right',
  },
  buttonGroup: {
    display: 'flex',
    justifyContent: 'center',
  },
  backButton: {
    padding: '1rem 2.5rem',
  },
  loading: {
    textAlign: 'center',
    paddingTop: '5rem',
    fontSize: '1.2rem',
  },
  alert: {
    backgroundColor: 'rgba(245, 158, 11, 0.1)',
    border: '1px solid rgba(245, 158, 11, 0.2)',
    color: '#fbbf24',
    padding: '0.8rem',
    borderRadius: '8px',
    marginBottom: '2rem',
    fontSize: '0.85rem',
    textAlign: 'center',
  }
};

export default Result;
