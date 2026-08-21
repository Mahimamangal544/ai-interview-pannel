import axios from 'axios';

const API_BASE = '/api';

const client = axios.create({
  baseURL: API_BASE,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const interviewApi = {
  // Auth
  login: async (credentials) => {
    const response = await client.post('/auth/login', credentials);
    return response.data;
  },

  register: async (details) => {
    const response = await client.post('/auth/register', details);
    return response.data;
  },

  // Interviews
  getUserInterviews: async (userId) => {
    const response = await client.get(`/interviews/user/${userId}`);
    return response.data;
  },

  createInterview: async (payload) => {
    const response = await client.post('/interviews', payload);
    return response.data;
  },

  getNextQuestion: async (interviewId, questionNumber) => {
    const response = await client.get(`/interviews/${interviewId}/next-question`, {
      params: { questionNumber }
    });
    return response.data;
  },

  submitAnswer: async (answerData) => {
    const response = await client.post('/interviews/answer', answerData);
    return response.data;
  },

  completeInterview: async (interviewId) => {
    const response = await client.post(`/interviews/${interviewId}/complete`);
    return response.data;
  },

  getInterviewResult: async (interviewId) => {
    const response = await client.get(`/interviews/${interviewId}/result`);
    return response.data;
  },
};
export default interviewApi;
