package com.interview.service;

import com.interview.entity.Answer;
import com.interview.entity.Interview;
import com.interview.entity.Question;
import com.interview.repository.AnswerRepository;
import com.interview.repository.InterviewRepository;
import com.interview.repository.QuestionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Map;

@Service
public class QuestionService {

    @Autowired
    private QuestionRepository questionRepository;

    @Autowired
    private InterviewRepository interviewRepository;

    @Autowired
    private AnswerRepository answerRepository;

    @Autowired
    private AIService aiService;

    public Question getOrCreateNextQuestion(Long interviewId, Integer questionNumber) {
        Interview interview = interviewRepository.findById(interviewId)
                .orElseThrow(() -> new RuntimeException("Interview session not found"));

        // If the question is already saved for this index range, fetch it
        List<Question> existingQuestions = questionRepository.findByInterviewId(interviewId);
        if (existingQuestions.size() >= questionNumber) {
            return existingQuestions.get(questionNumber - 1);
        }

        if (questionNumber == 1) {
            aiService.startInterview(interviewId, interview.getDifficulty());
            Map<String, String> aiQ = aiService.generateQuestion(interviewId, "Java", "OOP", interview.getDifficulty());
            
            Question q = new Question();
            q.setInterview(interview);
            q.setQuestionText(aiQ.getOrDefault("question", "What is inheritance in Java?"));
            q.setSkill(aiQ.getOrDefault("skill", "Java"));
            q.setTopic(aiQ.getOrDefault("topic", "OOP"));
            q.setDifficulty(aiQ.getOrDefault("difficulty", interview.getDifficulty()));
            return questionRepository.save(q);
        } else {
            // Find latest answer score to scale difficulty dynamically
            List<Answer> answers = answerRepository.findByInterviewId(interviewId);
            Double lastScore = 7.0; // Default fallback score
            if (!answers.isEmpty()) {
                lastScore = answers.get(answers.size() - 1).getFinalScore();
            }

            Map<String, String> aiQ = aiService.nextQuestion(interviewId, lastScore, interview.getDifficulty());
            
            Question q = new Question();
            q.setInterview(interview);
            q.setQuestionText(aiQ.getOrDefault("question", "What is a REST API?"));
            q.setSkill(aiQ.getOrDefault("skill", "Computer Networks"));
            q.setTopic(aiQ.getOrDefault("topic", "APIs"));
            q.setDifficulty(aiQ.getOrDefault("difficulty", "MEDIUM"));
            return questionRepository.save(q);
        }
    }
}
