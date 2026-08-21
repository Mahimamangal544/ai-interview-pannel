package com.interview.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "skill_scores", uniqueConstraints = {
    @UniqueConstraint(columnNames = {"interview_result_id", "skill"})
})
public class SkillScore {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "interview_result_id", nullable = false)
    private InterviewResult interviewResult;

    @Column(nullable = false, length = 50)
    private String skill;

    @Column(nullable = false)
    private Double score = 0.0;

    @Column(name = "evaluations_count", nullable = false)
    private Integer evaluationsCount = 0;

    public SkillScore() {}

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public InterviewResult getInterviewResult() { return interviewResult; }
    public void setInterviewResult(InterviewResult interviewResult) { this.interviewResult = interviewResult; }

    public String getSkill() { return skill; }
    public void setSkill(String skill) { this.skill = skill; }

    public Double getScore() { return score; }
    public void setScore(Double score) { this.score = score; }

    public Integer getEvaluationsCount() { return evaluationsCount; }
    public void setEvaluationsCount(Integer evaluationsCount) { this.evaluationsCount = evaluationsCount; }
}
