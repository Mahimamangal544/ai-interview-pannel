package com.interview.service;

import com.interview.dto.AnswerRequest;
import com.interview.dto.EvaluationResponse;
import com.interview.entity.Answer;
import com.interview.entity.Interview;
import com.interview.entity.Question;
import com.interview.repository.AnswerRepository;
import com.interview.repository.InterviewRepository;
import com.interview.repository.QuestionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class EvaluationService {

    @Autowired
    private AnswerRepository answerRepository;

    @Autowired
    private InterviewRepository interviewRepository;

    @Autowired
    private QuestionRepository questionRepository;

    @Autowired
    private AIService aiService;

    @Transactional
    public Answer evaluateAndSaveAnswer(AnswerRequest request) {
        Interview interview = interviewRepository.findById(request.getInterviewId())
                .orElseThrow(() -> new RuntimeException("Interview session not found"));

        Question question = questionRepository.findById(request.getQuestionId())
                .orElseThrow(() -> new RuntimeException("Question reference not found"));

        // Call Python AI Service for prompt-based answer evaluation
        EvaluationResponse eval = aiService.evaluateAnswer(
                interview.getId(), 
                question.getId(), 
                question.getQuestionText(), 
                request.getAnswerText()
        );

        // Check if an answer already exists to prevent duplicate submissions
        Answer answer = answerRepository.findByInterviewIdAndQuestionId(interview.getId(), question.getId())
                .orElse(new Answer());

        answer.setInterview(interview);
        answer.setQuestion(question);
        answer.setAnswerText(request.getAnswerText());
        answer.setCorrectness(eval.getCorrectness());
        answer.setTechnicalDepth(eval.getTechnicalDepth());
        answer.setClarity(eval.getClarity());
        answer.setCompleteness(eval.getCompleteness());
        answer.setFinalScore(eval.getFinalScore());
        answer.setFeedback(eval.getFeedback());

        return answerRepository.save(answer);
    }
}
