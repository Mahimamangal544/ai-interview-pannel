package com.interview.controller;

import com.interview.entity.Question;
import com.interview.repository.QuestionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/questions")
@CrossOrigin(origins = "*")
public class QuestionController {

    @Autowired
    private QuestionRepository questionRepository;

    @GetMapping("/interview/{interviewId}")
    public ResponseEntity<List<Question>> getQuestionsByInterview(@PathVariable Long interviewId) {
        return ResponseEntity.ok(questionRepository.findByInterviewId(interviewId));
    }

    @GetMapping("/{id}")
    public ResponseEntity<Question> getQuestionById(@PathVariable Long id) {
        return questionRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }
}
