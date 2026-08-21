package com.interview.service;

import com.interview.dto.EvaluationResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import java.util.HashMap;
import java.util.Map;

@Service
public class AIService {

    @Value("${ai.service.url:http://localhost:8000}")
    private String aiServiceUrl;

    private final RestTemplate restTemplate = new RestTemplate();

    public void startInterview(Long interviewId, String difficulty) {
        try {
            String url = aiServiceUrl + "/ai/start-interview";
            Map<String, Object> request = new HashMap<>();
            request.put("interview_id", interviewId);
            request.put("difficulty", difficulty);
            restTemplate.postForObject(url, request, String.class);
        } catch (Exception e) {
            System.err.println("Failed to contact AI service for start-interview: " + e.getMessage());
        }
    }

    @SuppressWarnings("unchecked")
    public Map<String, String> generateQuestion(Long interviewId, String skill, String topic, String difficulty) {
        try {
            String url = aiServiceUrl + "/ai/generate-question";
            Map<String, Object> request = new HashMap<>();
            request.put("interview_id", interviewId);
            request.put("skill", skill);
            request.put("topic", topic);
            request.put("difficulty", difficulty);
            return restTemplate.postForObject(url, request, Map.class);
        } catch (Exception e) {
            System.err.println("Failed to contact AI service for generate-question: " + e.getMessage());
            // Fallback mock question
            Map<String, String> fallback = new HashMap<>();
            fallback.put("question", "Explain the concept of OOP encapsulation and how you implement it in Java.");
            fallback.put("skill", "Java");
            fallback.put("topic", "OOP");
            fallback.put("difficulty", difficulty);
            return fallback;
        }
    }

    public EvaluationResponse evaluateAnswer(Long interviewId, Long questionId, String questionText, String answerText) {
        try {
            String url = aiServiceUrl + "/ai/evaluate-answer";
            Map<String, Object> request = new HashMap<>();
            request.put("interview_id", interviewId);
            request.put("question_id", questionId);
            request.put("question_text", questionText);
            request.put("answer_text", answerText);
            return restTemplate.postForObject(url, request, EvaluationResponse.class);
        } catch (Exception e) {
            System.err.println("Failed to contact AI service for evaluate-answer: " + e.getMessage());
            // Fallback mock evaluation
            return new EvaluationResponse(8.0, 7.0, 8.0, 7.0, 7.5, "Fallback feedback: Good description.");
        }
    }

    @SuppressWarnings("unchecked")
    public Map<String, String> nextQuestion(Long interviewId, Double lastScore, String difficulty) {
        try {
            String url = aiServiceUrl + "/ai/next-question";
            Map<String, Object> request = new HashMap<>();
            request.put("interview_id", interviewId);
            request.put("last_score", lastScore);
            request.put("difficulty", difficulty);
            return restTemplate.postForObject(url, request, Map.class);
        } catch (Exception e) {
            System.err.println("Failed to contact AI service for next-question: " + e.getMessage());
            Map<String, String> fallback = new HashMap<>();
            fallback.put("question", "How do indexes optimize query performance in MySQL database schemas?");
            fallback.put("skill", "MySQL");
            fallback.put("topic", "DBMS");
            fallback.put("difficulty", "MEDIUM");
            return fallback;
        }
    }

    @SuppressWarnings("unchecked")
    public Map<String, Object> finalReport(Long interviewId) {
        try {
            String url = aiServiceUrl + "/ai/final-report";
            Map<String, Object> request = new HashMap<>();
            request.put("interview_id", interviewId);
            return restTemplate.postForObject(url, request, Map.class);
        } catch (Exception e) {
            System.err.println("Failed to contact AI service for final-report: " + e.getMessage());
            Map<String, Object> fallback = new HashMap<>();
            fallback.put("summary", "Fallback summary: Strong grasp of core definitions.");
            fallback.put("recommendations", "Review indexing optimizations and time complexity metrics.");
            fallback.put("overall_score", 7.8);
            return fallback;
        }
    }
}
