package com.interview.controller;

import com.interview.dto.AnswerRequest;
import com.interview.dto.InterviewRequest;
import com.interview.entity.Answer;
import com.interview.entity.Interview;
import com.interview.entity.Question;
import com.interview.entity.InterviewResult;
import com.interview.service.EvaluationService;
import com.interview.service.InterviewService;
import com.interview.service.QuestionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/interviews")
@CrossOrigin(origins = "*")
public class InterviewController {

    @Autowired
    private InterviewService interviewService;

    @Autowired
    private QuestionService questionService;

    @Autowired
    private EvaluationService evaluationService;

    @PostMapping
    public ResponseEntity<Interview> createInterview(@RequestBody InterviewRequest request) {
        return ResponseEntity.ok(interviewService.createInterview(request));
    }

    @GetMapping("/user/{userId}")
    public ResponseEntity<List<Interview>> getInterviewsByUser(@PathVariable Long userId) {
        return ResponseEntity.ok(interviewService.getInterviewsByUserId(userId));
    }

    @GetMapping("/{id}/next-question")
    public ResponseEntity<Question> getNextQuestion(
            @PathVariable Long id, 
            @RequestParam(defaultValue = "1") Integer questionNumber) {
        return ResponseEntity.ok(questionService.getOrCreateNextQuestion(id, questionNumber));
    }

    @PostMapping("/answer")
    public ResponseEntity<Answer> submitAnswer(@RequestBody AnswerRequest request) {
        return ResponseEntity.ok(evaluationService.evaluateAndSaveAnswer(request));
    }

    @PostMapping("/{id}/complete")
    public ResponseEntity<InterviewResult> completeInterview(@PathVariable Long id) {
        return ResponseEntity.ok(interviewService.completeInterview(id));
    }

    @GetMapping("/{id}/result")
    public ResponseEntity<Map<String, Object>> getInterviewResult(@PathVariable Long id) {
        return ResponseEntity.ok(interviewService.getInterviewResultWithSkills(id));
    }
}
