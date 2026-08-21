import React from 'react';

const ChatWindow = ({ messages }) => {
  return (
    <div style={styles.container} className="glass-panel">
      <div style={styles.header}>
        <h3>Interview Conversation</h3>
      </div>
      <div style={styles.history}>
        {messages && messages.length > 0 ? (
          messages.map((msg, index) => (
            <div 
              key={index} 
              style={{
                ...styles.bubbleContainer,
                justifyContent: msg.sender === 'CANDIDATE' ? 'flex-end' : 'flex-start'
              }}
            >
              <div 
                style={{
                  ...styles.bubble,
                  backgroundColor: msg.sender === 'CANDIDATE' ? 'rgba(168, 85, 247, 0.2)' : 'rgba(56, 189, 248, 0.2)',
                  borderColor: msg.sender === 'CANDIDATE' ? '#a855f7' : '#38bdf8',
                }}
              >
                <div style={styles.sender}>{msg.sender === 'CANDIDATE' ? 'You' : 'Interviewer'}</div>
                <div style={styles.text}>{msg.text}</div>
                {msg.score !== undefined && (
                  <div style={styles.scoreBadge}>Score: {msg.score}/10</div>
                )}
              </div>
            </div>
          ))
        ) : (
          <div style={styles.empty}>No conversation history. The interview is about to start!</div>
        )}
      </div>
    </div>
  );
};

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    height: '400px',
    margin: '1rem 0',
    overflow: 'hidden',
  },
  header: {
    padding: '1rem',
    borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
  },
  history: {
    flex: 1,
    padding: '1rem',
    overflowY: 'auto',
    display: 'flex',
    flexDirection: 'column',
    gap: '1rem',
  },
  bubbleContainer: {
    display: 'flex',
    width: '100%',
  },
  bubble: {
    maxWidth: '70%',
    padding: '0.8rem 1.2rem',
    borderRadius: '12px',
    borderWidth: '1px',
    borderStyle: 'solid',
  },
  sender: {
    fontSize: '0.8rem',
    fontWeight: 'bold',
    marginBottom: '0.3rem',
    opacity: 0.8,
  },
  text: {
    fontSize: '0.95rem',
    lineHeight: '1.4',
  },
  scoreBadge: {
    fontSize: '0.75rem',
    marginTop: '0.4rem',
    padding: '2px 6px',
    borderRadius: '4px',
    background: 'rgba(0, 0, 0, 0.3)',
    display: 'inline-block',
  },
  empty: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100%',
    color: '#94a3b8',
    fontStyle: 'italic',
  }
};

export default ChatWindow;
