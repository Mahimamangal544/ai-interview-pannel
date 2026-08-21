package com.interview.dto;

public class AnswerRequest {
    private Long interviewId;
    private Long questionId;
    private String answerText;

    public AnswerRequest() {}

    public AnswerRequest(Long interviewId, Long questionId, String answerText) {
        this.interviewId = interviewId;
        this.questionId = questionId;
        this.answerText = answerText;
    }

    public Long getInterviewId() { return interviewId; }
    public void setInterviewId(Long interviewId) { this.interviewId = interviewId; }

    public Long getQuestionId() { return questionId; }
    public void setQuestionId(Long questionId) { this.questionId = questionId; }

    public String getAnswerText() { return answerText; }
    public void setAnswerText(String answerText) { this.answerText = answerText; }
}
