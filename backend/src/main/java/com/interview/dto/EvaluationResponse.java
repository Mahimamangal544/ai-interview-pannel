package com.interview.dto;

import com.fasterxml.jackson.annotation.JsonAlias;

public class EvaluationResponse {
    
    private Double correctness;

    @JsonAlias({"technical_depth", "technicalDepth"})
    private Double technicalDepth;

    private Double clarity;
    
    private Double completeness;

    @JsonAlias({"final_score", "finalScore"})
    private Double finalScore;

    private String feedback;

    public EvaluationResponse() {}

    public EvaluationResponse(Double correctness, Double technicalDepth, Double clarity, Double completeness, Double finalScore, String feedback) {
        this.correctness = correctness;
        this.technicalDepth = technicalDepth;
        this.clarity = clarity;
        this.completeness = completeness;
        this.finalScore = finalScore;
        this.feedback = feedback;
    }

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
}
