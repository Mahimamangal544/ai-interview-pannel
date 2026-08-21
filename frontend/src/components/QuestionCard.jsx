import React from 'react';

const QuestionCard = ({ question }) => {
  if (!question) return null;

  return (
    <div style={styles.card} className="glass-panel animate-fade-in">
      <div style={styles.header}>
        <span style={styles.badge}>{question.skill || 'General'}</span>
        <span style={{ ...styles.badge, ...styles.difficultyBadge(question.difficulty) }}>
          {question.difficulty || 'MEDIUM'}
        </span>
        <span style={styles.topic}>{question.topic || 'General Topic'}</span>
      </div>
      <h2 style={styles.text}>{question.questionText || question.question || 'No question prompt loaded.'}</h2>
    </div>
  );
};

const styles = {
  card: {
    padding: '1.5rem',
    marginBottom: '1rem',
  },
  header: {
    display: 'flex',
    gap: '0.8rem',
    alignItems: 'center',
    marginBottom: '1rem',
  },
  badge: {
    fontSize: '0.75rem',
    fontWeight: 'bold',
    padding: '4px 8px',
    borderRadius: '4px',
    backgroundColor: '#38bdf8',
    color: '#0f172a',
  },
  difficultyBadge: (diff) => {
    switch (diff?.toUpperCase()) {
      case 'EASY':
        return { backgroundColor: '#10b981', color: '#fff' };
      case 'HARD':
        return { backgroundColor: '#ef4444', color: '#fff' };
      default:
        return { backgroundColor: '#f59e0b', color: '#fff' };
    }
  },
  topic: {
    fontSize: '0.85rem',
    color: '#94a3b8',
  },
  text: {
    fontSize: '1.25rem',
    lineHeight: '1.5',
    margin: 0,
    fontWeight: '600',
  }
};

export default QuestionCard;
