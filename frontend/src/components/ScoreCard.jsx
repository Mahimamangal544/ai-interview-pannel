import React from 'react';

const ScoreCard = ({ evaluation }) => {
  if (!evaluation) return null;

  const metrics = [
    { label: 'Correctness', value: evaluation.correctness },
    { label: 'Technical Depth', value: evaluation.technicalDepth || evaluation.technical_depth },
    { label: 'Clarity', value: evaluation.clarity },
    { label: 'Completeness', value: evaluation.completeness },
  ];

  return (
    <div style={styles.card} className="glass-panel animate-fade-in">
      <h3 style={styles.title}>Answer Evaluation</h3>
      
      <div style={styles.metricsContainer}>
        {metrics.map((m, i) => (
          <div key={i} style={styles.metricRow}>
            <span style={styles.label}>{m.label}</span>
            <div style={styles.barBg}>
              <div 
                style={{ 
                  ...styles.barFill, 
                  width: `${(m.value || 0) * 10}%`,
                  backgroundColor: (m.value || 0) >= 7 ? '#10b981' : (m.value || 0) >= 4 ? '#f59e0b' : '#ef4444'
                }} 
              />
            </div>
            <span style={styles.value}>{m.value !== undefined ? `${m.value}/10` : 'N/A'}</span>
          </div>
        ))}
      </div>

      <div style={styles.overallContainer}>
        <div style={styles.overallLabel}>Overall Score</div>
        <div style={styles.overallScore}>{evaluation.finalScore || evaluation.final_score || 0}/10</div>
      </div>

      {evaluation.feedback && (
        <div style={styles.feedbackContainer}>
          <strong>AI Feedback:</strong>
          <p style={styles.feedbackText}>{evaluation.feedback}</p>
        </div>
      )}
    </div>
  );
};

const styles = {
  card: {
    padding: '1.5rem',
    margin: '1rem 0',
  },
  title: {
    margin: '0 0 1rem 0',
    fontSize: '1.2rem',
    borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
    paddingBottom: '0.5rem',
  },
  metricsContainer: {
    display: 'flex',
    flexDirection: 'column',
    gap: '0.8rem',
    marginBottom: '1.5rem',
  },
  metricRow: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    gap: '1rem',
  },
  label: {
    fontSize: '0.9rem',
    width: '120px',
    color: '#94a3b8',
  },
  barBg: {
    flex: 1,
    height: '8px',
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: '4px',
    overflow: 'hidden',
  },
  barFill: {
    height: '100%',
    borderRadius: '4px',
    transition: 'width 0.6s ease',
  },
  value: {
    fontSize: '0.9rem',
    fontWeight: 'bold',
    width: '45px',
    textAlign: 'right',
  },
  overallContainer: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '0.8rem 1rem',
    backgroundColor: 'rgba(56, 189, 248, 0.1)',
    border: '1px solid rgba(56, 189, 248, 0.3)',
    borderRadius: '8px',
    marginBottom: '1rem',
  },
  overallLabel: {
    fontWeight: 'bold',
    color: '#38bdf8',
  },
  overallScore: {
    fontSize: '1.5rem',
    fontWeight: '800',
    color: '#38bdf8',
  },
  feedbackContainer: {
    marginTop: '1rem',
    padding: '0.8rem',
    backgroundColor: 'rgba(255, 255, 255, 0.03)',
    borderRadius: '8px',
    fontSize: '0.9rem',
  },
  feedbackText: {
    margin: '0.3rem 0 0 0',
    color: '#cbd5e1',
    lineHeight: '1.4',
  }
};

export default ScoreCard;
