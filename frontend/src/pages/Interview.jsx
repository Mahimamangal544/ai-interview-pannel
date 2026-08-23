import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { interviewApi } from '../services/interviewApi';
import ProgressBar from '../components/ProgressBar';
import QuestionCard from '../components/QuestionCard';
import AnswerBox from '../components/AnswerBox';
import ScoreCard from '../components/ScoreCard';
import ChatWindow from '../components/ChatWindow';

const Interview = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [question, setQuestion] = useState(null);
  const [questionCount, setQuestionCount] = useState(1);
  const [totalQuestions] = useState(5); // Hardcoded limit for basic panel flow
  const [evaluation, setEvaluation] = useState(null);
  const [submitting, setSubmitting] = useState(false);
  const [chatMessages, setChatMessages] = useState([]);

  // Fetch the next question
  const fetchNextQuestion = async (currentCount) => {
    setLoading(true);
    setEvaluation(null);
    try {
      if (id === 'mock-123') {
        throw new Error('Using mock session');
      }
      // In a real application, the backend coordinates with Python AI to get the next question
      const q = await interviewApi.getNextQuestion(id, currentCount);
      setQuestion(q);
      
      // Append interviewer question to conversation log
      setChatMessages((prev) => [
        ...prev,
        { sender: 'AI', text: q.questionText || q.question || 'Next question...' }
      ]);
    } catch (err) {
      console.error(err);
      setError('Error loading question. Using local mock question.');
      
      // Local fallback Mock questions
      const mockQuestions = [
        { id: 101, questionText: 'What is inheritance in Java and how does it support OOP design?', skill: 'Java', topic: 'OOP', difficulty: 'EASY' },
        { id: 102, questionText: 'Explain the difference between primary keys, foreign keys, and unique keys in MySQL.', skill: 'MySQL', topic: 'DBMS', difficulty: 'MEDIUM' },
        { id: 103, questionText: 'How does Spring Boot manage dependency injection, and what are the main stereotypes annotations?', skill: 'Spring Boot', topic: 'Frameworks', difficulty: 'MEDIUM' },
        { id: 104, questionText: 'What is a binary search tree, and what is the time complexity of searching elements in it?', skill: 'Data Structures', topic: 'Algorithms', difficulty: 'HARD' },
        { id: 105, questionText: 'Explain how FastAPI leverages ASGI and Pydantic for high performance API schemas.', skill: 'Python', topic: 'FastAPI', difficulty: 'HARD' }
      ];
      
      const qIndex = Math.min(currentCount - 1, mockQuestions.length - 1);
      const fallbackQ = mockQuestions[qIndex];
      setQuestion(fallbackQ);
      setChatMessages((prev) => [
        ...prev,
        { sender: 'AI', text: fallbackQ.questionText }
      ]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchNextQuestion(1);
  }, [id]);

  const handleAnswerSubmit = async (answerText) => {
    setSubmitting(true);
    setError('');

    // Append candidate answer to conversation log
    setChatMessages((prev) => [
      ...prev,
      { sender: 'CANDIDATE', text: answerText }
    ]);

    try {
      if (id === 'mock-123') {
        throw new Error('Using mock session');
      }
      // Post answer evaluation request
      const evalData = await interviewApi.submitAnswer({
        interviewId: id,
        questionId: question.id || questionCount,
        answerText: answerText
      });

      setEvaluation(evalData);

      // Append score to latest candidate message in chat
      setChatMessages((prev) => {
        const copy = [...prev];
        if (copy.length > 0) {
          copy[copy.length - 1].score = evalData.finalScore || evalData.final_score;
        }
        return copy;
      });

    } catch (err) {
      console.error(err);
      setError('Failed to evaluate via backend. Showing local mock evaluation.');
      
      // Fallback Mock Evaluation
      const mockEval = {
        correctness: 8,
        technicalDepth: 7,
        clarity: 8,
        completeness: 7,
        finalScore: 7.5,
        feedback: 'Good description. You covered the base definitions well but could go slightly deeper into implementation details.'
      };
      setEvaluation(mockEval);

      setChatMessages((prev) => {
        const copy = [...prev];
        if (copy.length > 0) {
          copy[copy.length - 1].score = mockEval.finalScore;
        }
        return copy;
      });
    } finally {
      setSubmitting(false);
    }
  };

  const handleNext = () => {
    if (questionCount >= totalQuestions) {
      // Interview complete, route to results
      handleCompleteInterview();
    } else {
      const nextCount = questionCount + 1;
      setQuestionCount(nextCount);
      fetchNextQuestion(nextCount);
    }
  };

  const handleCompleteInterview = async () => {
    setLoading(true);
    try {
      if (id !== 'mock-123') {
        await interviewApi.completeInterview(id);
      }
      navigate(`/result/${id}`);
    } catch (err) {
      console.error(err);
      navigate(`/result/${id}`);
    }
  };

  return (
    <div className="container animate-fade-in" style={styles.container}>
      <header style={styles.header}>
        <h2>Technical AI Interview Session</h2>
        <button className="btn-secondary" onClick={handleCompleteInterview}>
          Exit & Complete
        </button>
      </header>

      {error && <div style={styles.alert}>{error}</div>}

      <div style={styles.layout}>
        <div style={styles.mainPane}>
          <ProgressBar current={questionCount} total={totalQuestions} />
          
          {loading ? (
            <div style={styles.loadingSpinner}>Loading Question...</div>
          ) : (
            <>
              <QuestionCard question={question} />
              
              {!evaluation && (
                <AnswerBox onSubmit={handleAnswerSubmit} isDisabled={submitting} />
              )}

              {evaluation && (
                <div className="animate-fade-in">
                  <ScoreCard evaluation={evaluation} />
                  <button 
                    onClick={handleNext} 
                    className="btn-primary" 
                    style={styles.nextButton}
                  >
                    {questionCount >= totalQuestions ? 'Finish and View Results' : 'Proceed to Next Question'}
                  </button>
                </div>
              )}
            </>
          )}
        </div>

        <aside style={styles.chatPane}>
          <ChatWindow messages={chatMessages} />
        </aside>
      </div>
    </div>
  );
};

const styles = {
  container: {
    paddingTop: '2rem',
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '2rem',
  },
  layout: {
    display: 'grid',
    gridTemplateColumns: '1.2fr 0.8fr',
    gap: '2.5rem',
  },
  mainPane: {
    display: 'flex',
    flexDirection: 'column',
  },
  chatPane: {
    height: '100%',
  },
  nextButton: {
    marginTop: '1rem',
    width: '100%',
  },
  loadingSpinner: {
    textAlign: 'center',
    padding: '3rem',
    fontSize: '1.2rem',
    color: '#94a3b8',
  },
  alert: {
    backgroundColor: 'rgba(245, 158, 11, 0.1)',
    border: '1px solid rgba(245, 158, 11, 0.2)',
    color: '#fbbf24',
    padding: '0.8rem',
    borderRadius: '8px',
    marginBottom: '1.5rem',
    fontSize: '0.9rem',
  }
};

export default Interview;
