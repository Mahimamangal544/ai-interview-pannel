# Coordinated AI Interview Panel - Project Folder Structure & File Guide

This document provides a comprehensive overview of the **Coordinated AI Interview Panel** repository structure, detailed file function descriptions, and compilation/execution commands.

---

## 📁 Repository Directory Tree

```text
coordinated-ai-interview-panel/
│
├── frontend/                             # React + Vite Frontend Web Application
│   ├── src/
│   │   ├── components/                   # Reusable UI Components
│   │   │   ├── ChatWindow.jsx            # Dialogue history component between AI & candidate
│   │   │   ├── QuestionCard.jsx          # Displays active question, topic tags, and difficulty
│   │   │   ├── AnswerBox.jsx             # Text input form for candidate answer submission
│   │   │   ├── ScoreCard.jsx             # Displays evaluation score metrics and AI feedback
│   │   │   └── ProgressBar.jsx           # Interview progress indicator bar
│   │   │
│   │   ├── pages/                        # View Pages / Routes
│   │   │   ├── Login.jsx                 # User login and registration form page
│   │   │   ├── Dashboard.jsx             # Overview dashboard for past interviews & stats
│   │   │   ├── InterviewSetup.jsx        # Configuration screen for launching new sessions
│   │   │   ├── Interview.jsx             # Main interactive interview page loop
│   │   │   └── Result.jsx                # Final performance report & recommendations page
│   │   │
│   │   ├── services/
│   │   │   └── interviewApi.js           # Axios API client connecting Frontend to Spring Boot
│   │   │
│   │   ├── App.jsx                       # Main React Router setup and authentication state
│   │   ├── main.jsx                      # React DOM root entry script
│   │   └── index.css                     # Global CSS styling system (Dark mode & glassmorphism)
│   │
│   ├── index.html                        # Main HTML template for Vite
│   ├── package.json                      # Node.js dependencies and script definitions
│   └── vite.config.js                    # Vite server configuration & API proxy setup
│
├── backend/                              # Java + Spring Boot Backend Core
│   ├── src/main/java/com/interview/
│   │   ├── InterviewApplication.java     # Spring Boot application main entry class
│   │   │
│   │   ├── config/
│   │   │   └── SecurityConfig.java       # Spring Security filters and PasswordEncoder bean
│   │   │
│   │   ├── controller/
│   │   │   ├── AuthController.java       # User authentication REST endpoints (/api/auth)
│   │   │   ├── InterviewController.java  # Session & interview workflow REST endpoints (/api/interviews)
│   │   │   ├── QuestionController.java   # Question query REST endpoints (/api/questions)
│   │   │   └── ResultController.java     # Evaluation report REST endpoints (/api/results)
│   │   │
│   │   ├── service/
│   │   │   ├── AIService.java            # RestTemplate HTTP client invoking Python FastAPI
│   │   │   ├── InterviewService.java     # Business logic for interview initialization & final report
│   │   │   ├── QuestionService.java      # Manages question sequence & adaptive difficulty
│   │   │   └── EvaluationService.java    # Handles answer grading & evaluation persistence
│   │   │
│   │   ├── repository/
│   │   │   ├── UserRepository.java       # JPA database repository for User entity
│   │   │   ├── InterviewRepository.java  # JPA database repository for Interview entity
│   │   │   ├── QuestionRepository.java   # JPA database repository for Question entity
│   │   │   ├── AnswerRepository.java     # JPA database repository for Answer entity
│   │   │   ├── InterviewResultRepository.java # JPA repository for InterviewResult entity
│   │   │   └── SkillScoreRepository.java # JPA repository for SkillScore entity
│   │   │
│   │   ├── entity/
│   │   │   ├── User.java                 # JPA Entity for candidate credentials & roles
│   │   │   ├── Interview.java            # JPA Entity for interview session state
│   │   │   ├── Question.java             # JPA Entity for generated question metadata
│   │   │   ├── Answer.java               # JPA Entity for candidate answers & grades
│   │   │   ├── InterviewResult.java      # JPA Entity for overall performance report
│   │   │   └── SkillScore.java           # JPA Entity for per-skill performance matrix
│   │   │
│   │   └── dto/
│   │       ├── InterviewRequest.java     # Data Transfer Object for creating interviews
│   │       ├── AnswerRequest.java        # Data Transfer Object for submitting answers
│   │       └── EvaluationResponse.java   # Data Transfer Object for AI score response
│   │
│   ├── src/main/resources/
│   │   └── application.properties        # Database connections, server port & AI service URL
│   └── pom.xml                           # Maven dependencies (Spring Web, Data JPA, Security, MySQL)
│
├── ai-service/                           # Python + FastAPI AI Adapter Service
│   ├── app/
│   │   ├── main.py                       # FastAPI application entrypoint and middleware
│   │   ├── session_store.py              # Shared in-memory session tracking module
│   │   │
│   │   ├── routes/
│   │   │   ├── interview.py              # Endpoints: /ai/start-interview, /ai/final-report
│   │   │   ├── evaluation.py             # Endpoints: /ai/evaluate-answer
│   │   │   └── question.py               # Endpoints: /ai/generate-question, /ai/next-question
│   │   │
│   │   ├── services/
│   │   │   ├── llm_service.py            # Interfaces with LLM API or returns mock evaluation payload
│   │   │   ├── question_service.py       # Adaptive difficulty logic & question pool selection
│   │   │   ├── evaluation_service.py     # Coordinates answer grading workflows
│   │   │   ├── scoring_service.py        # Calculates score averages and aggregate metrics
│   │   │   └── recommendation_service.py # Formulates qualitative summary & recommendations
│   │   │
│   │   ├── models/
│   │   │   ├── schemas.py                # Pydantic request and response schemas
│   │   │   └── prompts.py                # Prompt templates for question generation & evaluation
│   │   │
│   │   ├── rag/
│   │   │   ├── embeddings.py             # Embeddings generator scaffolding
│   │   │   ├── vector_store.py           # Vector similarity store scaffolding
│   │   │   └── retriever.py              # Context retrieval pipeline scaffolding
│   │   │
│   │   └── utils/
│   │       └── __init__.py               # Utilities package initializer
│   │
│   ├── datasets/
│   │   ├── questions.json                # Pre-populated questions dataset
│   │   ├── interview_answers.json        # Sample candidate answer responses
│   │   └── evaluation_dataset.json       # Ground-truth evaluation benchmarks
│   │
│   ├── training/
│   │   ├── prepare_dataset.py            # Dataset preprocessing script
│   │   ├── train.py                      # Model fine-tuning pipeline scaffold
│   │   └── evaluate.py                   # Checkpoint evaluation script
│   │
│   ├── tests/
│   │   ├── test_question.py              # Unit tests for QuestionService adaptivity
│   │   ├── test_evaluation.py            # Unit tests for EvaluationService outputs
│   │   └── test_scoring.py               # Unit tests for ScoringService averages
│   │
│   ├── requirements.txt                  # Python dependencies (fastapi, uvicorn, pydantic, pytest)
│   └── README.md                         # AI Service setup documentation
│
├── database/
│   └── schema.sql                        # MySQL database DDL (Tables, Indexes, Constraints)
│
├── docs/
│   └── architecture.md                   # Architecture specification & sequence diagrams
│
├── .gitignore                            # Standard Git ignore configurations
├── FOLDER_STRUCTURE.md                   # Detailed folder structure documentation (This file)
└── README.md                             # Root project README
```

---

## 🛠️ Detailed File & Function Breakdown

### 1. Root Directory

| File Path | Description / Function |
| :--- | :--- |
| `README.md` | Top-level documentation containing project overview, architecture diagram, env variables, and quickstart commands. |
| `FOLDER_STRUCTURE.md` | Comprehensive file-by-file function index and run guide. |
| `.gitignore` | Prevents binary targets (`target/`), dependencies (`node_modules/`, `venv/`), and secrets (`.env`) from being committed to Git. |
| `database/schema.sql` | DDL script defining tables (`users`, `interviews`, `questions`, `answers`, `interview_results`, `skill_scores`) with primary/foreign keys and indexes. |
| `docs/architecture.md` | Sequence diagrams and component responsibility descriptions. |

---

### 2. Frontend (`frontend/`)

| File Path | Description / Function |
| :--- | :--- |
| `frontend/vite.config.js` | Configures Vite server on port 3000 and proxies `/api` requests to Spring Boot (`http://localhost:8080`). |
| `frontend/package.json` | Defines React, React Router DOM, Axios, and Vite dependencies and build scripts. |
| `frontend/index.html` | Entry HTML document rendering `#root` container. |
| `frontend/src/main.jsx` | Initializes React application root. |
| `frontend/src/App.jsx` | Handles top-level routing, route protection guards, and login state management. |
| `frontend/src/index.css` | Implements glassmorphism aesthetic styling system with CSS custom properties and dark mode rules. |
| `frontend/src/services/interviewApi.js` | Axios HTTP client executing REST calls (`/api/auth`, `/api/interviews`, `/api/interviews/answer`). |
| `frontend/src/components/ChatWindow.jsx` | Renders dynamic chat bubble dialogue history between interviewer AI and candidate. |
| `frontend/src/components/QuestionCard.jsx` | Displays current question prompt, skill tags, topic, and difficulty level badges. |
| `frontend/src/components/AnswerBox.jsx` | Interactive text area input form for submitting technical answers. |
| `frontend/src/components/ScoreCard.jsx` | Renders immediate visual breakdown of correctness, technical depth, clarity, completeness, and feedback. |
| `frontend/src/components/ProgressBar.jsx` | Displays question index progress (e.g. Question 3 of 5). |
| `frontend/src/pages/Login.jsx` | User authentication interface handling candidate sign-in and sign-up. |
| `frontend/src/pages/Dashboard.jsx` | Main dashboard displaying past interview history, status badges, and aggregate statistics. |
| `frontend/src/pages/InterviewSetup.jsx` | Form page allowing candidate to configure title and target starting difficulty. |
| `frontend/src/pages/Interview.jsx` | Primary interview session container managing question fetch, answer submission, and chat history. |
| `frontend/src/pages/Result.jsx` | Final report view showing overall grade gauge, summary text, recommendations, and skill performance bars. |

---

### 3. Spring Boot Backend (`backend/`)

| File Path | Description / Function |
| :--- | :--- |
| `backend/pom.xml` | Maven build specification defining Spring Boot starter dependencies (Web, Data JPA, Security, MySQL). |
| `backend/src/main/resources/application.properties` | Configures database connection strings, Hibernate properties, and Python AI service host URL. |
| `backend/.../InterviewApplication.java` | Spring Boot main entrypoint class. |
| `backend/.../config/SecurityConfig.java` | Disables default CSRF for REST APIs, permits endpoint routes, and exposes PasswordEncoder bean. |
| `backend/.../controller/AuthController.java` | Exposes `/api/auth/register` and `/api/auth/login` REST endpoints. |
| `backend/.../controller/InterviewController.java` | Exposes `/api/interviews` endpoints for starting sessions, fetching questions, submitting answers, and completing interviews. |
| `backend/.../controller/QuestionController.java` | Exposes `/api/questions` endpoints for entity lookups. |
| `backend/.../controller/ResultController.java` | Exposes `/api/results` endpoints for querying performance reports. |
| `backend/.../service/AIService.java` | Uses Spring `RestTemplate` to call Python FastAPI endpoints (`/ai/start-interview`, `/ai/evaluate-answer`, etc.) with fallback handlers. |
| `backend/.../service/InterviewService.java` | Manages interview session lifecycle, calculates skill averages, and constructs overall results. |
| `backend/.../service/QuestionService.java` | Manages question sequencing and queries adaptive next questions based on past performance scores. |
| `backend/.../service/EvaluationService.java` | Persists graded candidate answers into MySQL via `AnswerRepository`. |
| `backend/.../repository/*` | JPA repository interfaces (`UserRepository`, `InterviewRepository`, `QuestionRepository`, `AnswerRepository`, `InterviewResultRepository`, `SkillScoreRepository`). |
| `backend/.../entity/*` | Database entity models (`User`, `Interview`, `Question`, `Answer`, `InterviewResult`, `SkillScore`). |
| `backend/.../dto/*` | Data transfer objects (`InterviewRequest`, `AnswerRequest`, `EvaluationResponse`). |

---

### 4. Python AI Service (`ai-service/`)

| File Path | Description / Function |
| :--- | :--- |
| `ai-service/requirements.txt` | Python dependencies (`fastapi`, `uvicorn`, `pydantic`, `pytest`, `python-dotenv`). |
| `ai-service/app/main.py` | FastAPI application entry point, mounts routes and configures CORS middleware. |
| `ai-service/app/session_store.py` | Shared in-memory dictionary storing session states to prevent circular imports. |
| `ai-service/app/routes/interview.py` | Router exposing `/ai/start-interview` and `/ai/final-report`. |
| `ai-service/app/routes/question.py` | Router exposing `/ai/generate-question` and `/ai/next-question`. |
| `ai-service/app/routes/evaluation.py` | Router exposing `/ai/evaluate-answer`. |
| `ai-service/app/services/llm_service.py` | Interfaces with LLM API or provides structured mock evaluation payloads. |
| `ai-service/app/services/question_service.py` | Implements adaptive routing logic (Score < 5 -> EASY, Score > 8 -> HARD). |
| `ai-service/app/services/evaluation_service.py` | Handles grading prompt processing. |
| `ai-service/app/services/scoring_service.py` | Computes historical performance averages. |
| `ai-service/app/services/recommendation_service.py` | Formulates qualitative summary reports and recommendation feedback. |
| `ai-service/app/models/schemas.py` | Pydantic schemas validating input/output payloads. |
| `ai-service/app/models/prompts.py` | LLM prompt templates for evaluations and question generation. |
| `ai-service/app/rag/*` | Scaffolding for text vectorization (`embeddings.py`), store (`vector_store.py`), and retrieval (`retriever.py`). |
| `ai-service/datasets/*` | Dataset storage (`questions.json`, `interview_answers.json`, `evaluation_dataset.json`). |
| `ai-service/training/*` | Scaffolding scripts for preprocessing dataset (`prepare_dataset.py`), fine-tuning (`train.py`), and checkpoint assessment (`evaluate.py`). |
| `ai-service/tests/*` | Pytest unit test suites (`test_question.py`, `test_evaluation.py`, `test_scoring.py`). |

---

## 🚀 Compilation & Running Commands

### 1. Database Setup
Create database and apply schema:
```bash
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS interview_panel;"
mysql -u root -p interview_panel < database/schema.sql
```

---

### 2. Python AI Service

**Setup & Install:**
```bash
cd ai-service
python -m venv venv
venv\Scripts\activate            # On Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
```

**Run Unit Tests:**
```bash
python -m pytest tests/ -v
```

**Run FastAPI Server:**
```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
*API docs available at: `http://localhost:8000/docs`*

---

### 3. Spring Boot Backend

**Compile Code:**
```bash
cd backend
mvn clean compile
```

**Run Spring Boot Server:**
```bash
mvn spring-boot:run
```
*Backend runs on: `http://localhost:8080`*

---

### 4. React Frontend

**Install Dependencies:**
```bash
cd frontend
npm install
```

**Production Build Verification:**
```bash
npm run build
```

**Run Vite Development Server:**
```bash
npm run dev
```
*Frontend runs on: `http://localhost:3000`*
