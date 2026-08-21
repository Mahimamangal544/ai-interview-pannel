package com.interview.dto;

public class InterviewRequest {
    private Long userId;
    private String title;
    private String difficulty;

    public InterviewRequest() {}

    public InterviewRequest(Long userId, String title, String difficulty) {
        this.userId = userId;
        this.title = title;
        this.difficulty = difficulty;
    }

    public Long getUserId() { return userId; }
    public void setUserId(Long userId) { this.userId = userId; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getDifficulty() { return difficulty; }
    public void setDifficulty(String difficulty) { this.difficulty = difficulty; }
}
