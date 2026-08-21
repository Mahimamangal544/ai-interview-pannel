package com.interview.controller;

import com.interview.entity.InterviewResult;
import com.interview.repository.InterviewResultRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/results")
@CrossOrigin(origins = "*")
public class ResultController {

    @Autowired
    private InterviewResultRepository resultRepository;

    @GetMapping("/interview/{interviewId}")
    public ResponseEntity<InterviewResult> getResultByInterview(@PathVariable Long interviewId) {
        return resultRepository.findByInterviewId(interviewId)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/{id}")
    public ResponseEntity<InterviewResult> getResultById(@PathVariable Long id) {
        return resultRepository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }
}
