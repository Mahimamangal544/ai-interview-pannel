-- Create Database if not exists
CREATE DATABASE IF NOT EXISTS interview_panel;
USE interview_panel;

-- 1. Users Table
CREATE TABLE IF NOT EXISTS users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'CANDIDATE',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_users_username (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 2. Interviews Table
CREATE TABLE IF NOT EXISTS interviews (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    title VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'PENDING', -- PENDING, ONGOING, COMPLETED, CANCELLED
    difficulty VARCHAR(20) NOT NULL DEFAULT 'MEDIUM', -- EASY, MEDIUM, HARD
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_interviews_user (user_id),
    INDEX idx_interviews_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 3. Questions Table (Storage of pool/generated questions)
CREATE TABLE IF NOT EXISTS questions (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    interview_id BIGINT NOT NULL,
    question_text TEXT NOT NULL,
    skill VARCHAR(50) NOT NULL,
    topic VARCHAR(100) NOT NULL,
    difficulty VARCHAR(20) NOT NULL, -- EASY, MEDIUM, HARD
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (interview_id) REFERENCES interviews(id) ON DELETE CASCADE,
    INDEX idx_questions_interview (interview_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4. Answers Table (Candidate answers linked to questions)
CREATE TABLE IF NOT EXISTS answers (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    interview_id BIGINT NOT NULL,
    question_id BIGINT NOT NULL,
    answer_text TEXT NOT NULL,
    correctness DOUBLE NOT NULL DEFAULT 0.0,
    technical_depth DOUBLE NOT NULL DEFAULT 0.0,
    clarity DOUBLE NOT NULL DEFAULT 0.0,
    completeness DOUBLE NOT NULL DEFAULT 0.0,
    final_score DOUBLE NOT NULL DEFAULT 0.0,
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (interview_id) REFERENCES interviews(id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE,
    UNIQUE KEY uq_interview_question (interview_id, question_id),
    INDEX idx_answers_interview (interview_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 5. Interview Results Table (Overall result summary)
CREATE TABLE IF NOT EXISTS interview_results (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    interview_id BIGINT NOT NULL UNIQUE,
    user_id BIGINT NOT NULL,
    overall_score DOUBLE NOT NULL DEFAULT 0.0,
    summary TEXT,
    recommendations TEXT,
    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (interview_id) REFERENCES interviews(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_results_user (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 6. Skill Scores Table (Breakdown of performance per skill)
CREATE TABLE IF NOT EXISTS skill_scores (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    interview_result_id BIGINT NOT NULL,
    skill VARCHAR(50) NOT NULL,
    score DOUBLE NOT NULL DEFAULT 0.0,
    evaluations_count INT NOT NULL DEFAULT 0,
    FOREIGN KEY (interview_result_id) REFERENCES interview_results(id) ON DELETE CASCADE,
    UNIQUE KEY uq_result_skill (interview_result_id, skill)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
