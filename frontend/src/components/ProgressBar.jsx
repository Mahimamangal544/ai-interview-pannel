import React from 'react';

const ProgressBar = ({ current, total }) => {
  const percentage = total > 0 ? Math.min(100, Math.max(0, (current / total) * 100)) : 0;

  return (
    <div style={styles.container}>
      <div style={styles.textContainer}>
        <span style={styles.label}>Interview Progress</span>
        <span style={styles.fraction}>
          Question {current} of {total}
        </span>
      </div>
      <div style={styles.track}>
        <div style={{ ...styles.bar, width: `${percentage}%` }} />
      </div>
    </div>
  );
};

const styles = {
  container: {
    margin: '1rem 0',
    width: '100%',
  },
  textContainer: {
    display: 'flex',
    justifyContent: 'space-between',
    marginBottom: '0.5rem',
    fontSize: '0.9rem',
  },
  label: {
    color: '#94a3b8',
    fontWeight: '500',
  },
  fraction: {
    fontWeight: 'bold',
    color: '#38bdf8',
  },
  track: {
    height: '6px',
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: '3px',
    overflow: 'hidden',
  },
  bar: {
    height: '100%',
    backgroundColor: '#38bdf8',
    borderRadius: '3px',
    transition: 'width 0.4s ease',
  }
};

export default ProgressBar;
