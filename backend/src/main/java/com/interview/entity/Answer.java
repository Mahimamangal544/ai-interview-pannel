package com.interview.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "answers", uniqueConstraints = {
    @UniqueConstraint(columnNames = {"interview_id", "question_id"})
})
public class Answer {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "interview_id", nullable = false)
    private Interview interview;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "question_id", nullable = false)
    private Question question;

    @Column(name = "answer_text", nullable = false, columnDefinition = "TEXT")
    private String answerText;

    @Column(nullable = false)
    private Double correctness = 0.0;

    @Column(name = "technical_depth", nullable = false)
    private Double technicalDepth = 0.0;

    @Column(nullable = false)
    private Double clarity = 0.0;

    @Column(nullable = false)
    private Double completeness = 0.0;

    @Column(name = "final_score", nullable = false)
    private Double finalScore = 0.0;

    @Column(columnDefinition = "TEXT")
    private String feedback;

    @Column(name = "created_at", updatable = false)
    private LocalDateTime createdAt = LocalDateTime.now();

    public Answer() {}

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public Interview getInterview() { return interview; }
    public void setInterview(Interview interview) { this.interview = interview; }

    public Question getQuestion() { return question; }
    public void setQuestion(Question question) { this.question = question; }

    public String getAnswerText() { return answerText; }
    public void setAnswerText(String answerText) { this.answerText = answerText; }

    public Double getCorrectness() { return correctness; }
    public void setCorrectness(Double correctness) { this.correctness = correctness; }

    public Double getTechnicalDepth() { return technicalDepth; }
    public void setTechnicalDepth(Double technicalDepth) { this.technicalDepth = technicalDepth; }

    public Double getClarity() { return clarity; }
    public void setClarity(Double clarity) { this.clarity = clarity; }

    public Double getCompleteness() { return completeness; }
    public void setCompleteness(Double completeness) { this.completeness = completeness; }

    public Double getFinalScore() { return finalScore; }
    public void setFinalScore(Double finalScore) { this.finalScore = finalScore; }

    public String getFeedback() { return feedback; }
    public void setFeedback(String feedback) { this.feedback = feedback; }

    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}
