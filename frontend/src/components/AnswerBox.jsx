import React, { useState } from 'react';

const AnswerBox = ({ onSubmit, isDisabled }) => {
  const [answer, setAnswer] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!answer.trim()) return;
    onSubmit(answer);
    setAnswer('');
  };

  return (
    <form onSubmit={handleSubmit} style={styles.form}>
      <textarea
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
        placeholder="Type your detailed answer here..."
        disabled={isDisabled}
        rows={5}
        style={styles.textarea}
      />
      <button 
        type="submit" 
        disabled={isDisabled || !answer.trim()} 
        className="btn-primary"
        style={styles.button}
      >
        {isDisabled ? 'Submitting Answer...' : 'Submit Answer'}
      </button>
    </form>
  );
};

const styles = {
  form: {
    display: 'flex',
    flexDirection: 'column',
    gap: '1rem',
    margin: '1rem 0',
  },
  textarea: {
    resize: 'vertical',
    fontSize: '1rem',
    minHeight: '120px',
  },
  button: {
    alignSelf: 'flex-end',
  }
};

export default AnswerBox;
