# Coordinated AI Interview Panel - Technical Interview Flow

This document details the complete end-to-end working of the adaptive technical interview process within the AI Service backend.

## 1. Interview Initialization
**Endpoint:** `POST /ai/start-interview`
*   The client initiates a new interview session by sending the `interview_id`, `role`, `skill`, `topic`, and initial `difficulty` level (e.g., "MEDIUM").
*   An in-memory session is created to track the candidate's progress throughout the interview. This session stores their details, initializes a history of `asked_questions`, and maintains a record of their `scores`.

## 2. Question Generation
**Endpoint:** `POST /ai/generate-question` (Initial) & `POST /ai/next-question` (Subsequent)
*   The system uses the current session parameters (`role`, `skill`, `topic`, `difficulty`) and the history of `previously_asked_questions` to request a unique question.
*   **AI Generation:** An LLM (configured via the Groq/OpenAI integration in `LLMService`) dynamically generates a question directly targeting the requested criteria. 
*   **Graceful Fallback:** If the API key is not configured or the LLM request fails, the system automatically falls back to a predefined local `question_pool`, matching against the requested skill, topic, and difficulty.
*   Once generated, the question is logged in the session's `asked_questions` list to guarantee no repetition.

## 3. Answer Evaluation
**Endpoint:** `POST /ai/evaluate-answer`
*   When a candidate submits their answer, the backend forwards the question, the candidate's answer, and any expected concepts to the evaluation endpoint.
*   The system uses a strict evaluation prompt instructing the LLM to act as an expert technical interviewer. The LLM objectively grades the answer on a scale from 0 to 10 across five dimensions:
    1.  `correctness`
    2.  `technical_depth`
    3.  `clarity`
    4.  `completeness`
    5.  `problem_solving`
*   The LLM returns a structured JSON containing these individual scores, a `final_score` (the average), and short constructive `feedback`.
*   The `final_score` is appended to the session's scores list, and the full detailed evaluation record is persisted in the central `EvaluationStore`.

## 4. Adaptive Difficulty
**Endpoint:** `POST /ai/next-question`
*   Before generating a subsequent question, the system analyzes the candidate's performance on the immediately preceding question.
*   The difficulty level adapts dynamically:
    *   **Score < 5.0:** The difficulty is lowered to `EASY` to help the candidate regain their footing.
    *   **Score >= 8.0:** The difficulty is promoted to the next tier (e.g., from `EASY` to `MEDIUM`, or `MEDIUM` to `HARD`) to appropriately challenge strong candidates.
    *   **Scores between 5.0 and 7.9:** The current difficulty level is maintained.
*   The session's difficulty state is updated, and a new question matching this updated difficulty is generated.

## 5. Final Report Generation
**Endpoint:** `POST /api/final-report`
*   At the conclusion of the interview, the client requests a final evaluation report.
*   The system retrieves all granular evaluation records from the `EvaluationStore` for the specific `interview_id`.
*   **Skill Analysis:** The `SkillAnalysisService` aggregates all evaluations. It scales scores to a 0-100 percentage basis, calculates the overall technical score, and computes the average score per individual skill.
    *   **Strengths** are identified as skills scoring 80% or higher.
    *   **Weaknesses** are identified as skills scoring below 60%.
*   **Recommendations:** The `RecommendationService` takes the analyzed skill metrics and generates personalized, actionable recommendations for the candidate (e.g., focusing on fundamentals vs. practicing advanced implementation).
*   A comprehensive final report encompassing the overall score, strengths, weaknesses, a textual summary, and customized recommendations is returned to the client.
