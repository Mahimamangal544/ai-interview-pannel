# Coordinated AI Interview Panel

An AI-driven technical mock interview platform that adapts questions dynamically based on candidates' response evaluations.

## Project Architecture

The system is structured as three decoupled services:
1. **Frontend**: React + Vite (Web UI interface)
2. **Backend**: Spring Boot + Data JPA + MySQL (Core business logic, scheduling, database state management)
3. **AI Service**: Python + FastAPI (Adapter service to evaluate answers and generate adaptive follow-up questions)

```
React Frontend
      │ (REST APIs)
      ▼
Spring Boot Backend ───(HTTP)───► Python AI Service
      │                                  │
      ▼ (JPA)                            ▼ (LLM / RAG Logic)
  MySQL DB                          AI evaluation & selection
```

---

## Technologies Used

- **Frontend**: React (JavaScript), Vite, Axios
- **Backend**: Spring Boot 3.x, Maven, JPA/Hibernate, MySQL Driver, Spring Security, Lombok
- **AI Service**: Python 3.10+, FastAPI, Uvicorn, Pydantic, python-dotenv
- **Database**: MySQL 8.x

---

## Folder Structure

```
coordinated-ai-interview-panel/
├── frontend/             # React (Vite) UI Client
├── backend/              # Maven Spring Boot Core Service
├── ai-service/           # FastAPI Python AI and NLP Engine
├── database/             # Schema definitions
│   └── schema.sql
├── docs/                 # Documentation and diagrams
└── README.md
```

---

## How to Run

### 1. Database Setup
Create a MySQL database named `interview_panel` and execute the schema:
```bash
mysql -u root -p interview_panel < database/schema.sql
```

### 2. Run Python AI Service
1. Navigate to `ai-service`
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the server:
   ```bash
   uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
   ```

### 3. Run Spring Boot Backend
1. Navigate to `backend`
2. Configure credentials in `src/main/resources/application.properties` (or export as env vars)
3. Run with Maven:
   ```bash
   mvn spring-boot:run
   ```

### 4. Run React Frontend
1. Navigate to `frontend`
2. Install npm modules:
   ```bash
   npm install
   ```
3. Run Vite server:
   ```bash
   npm run dev
   ```

---

## Required Environment Variables

Ensure these environment variables or configuration properties are set before running the applications:

### Spring Boot Backend (`backend/src/main/resources/application.properties`):
- `SPRING_DATASOURCE_URL` (Default: `jdbc:mysql://localhost:3606/interview_panel`)
- `SPRING_DATASOURCE_USERNAME` (Default: `root`)
- `SPRING_DATASOURCE_PASSWORD`
- `AI_SERVICE_URL` (Default: `http://localhost:8000`)

### Python AI Service (`ai-service/.env`):
- `OPENAI_API_KEY` (Required for LLM evaluation, otherwise falls back to Mock)
- `PORT` (Default: `8000`)

---

## Primary AI Service Endpoints

- `POST /ai/start-interview` - Initial setup profile details.
- `POST /ai/generate-question` - Fetches/generates the initial question.
- `POST /ai/evaluate-answer` - Grades correctness, depth, clarity, completeness.
- `POST /ai/next-question` - Fetches next adaptive question based on scoring history.
- `POST /ai/final-report` - Aggregates performance, details final scores & feedback.
