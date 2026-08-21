import random
from typing import Dict, Any, List

class QuestionService:
    def __init__(self):
        # Local fallback question pool
        self.question_pool = [
            {"question": "What is inheritance in Java?", "skill": "Java", "topic": "OOP", "difficulty": "EASY"},
            {"question": "What are the rules of encapsulation in Java?", "skill": "Java", "topic": "OOP", "difficulty": "EASY"},
            {"question": "Explain the difference between HashMap and TreeMap in Java.", "skill": "Java", "topic": "Data Structures", "difficulty": "MEDIUM"},
            {"question": "How does Spring Boot resolve dependency injection cycles?", "skill": "Spring Boot", "topic": "Core", "difficulty": "MEDIUM"},
            {"question": "What are the ACID properties in database management systems?", "skill": "MySQL", "topic": "DBMS", "difficulty": "MEDIUM"},
            {"question": "How do database indexes speed up query performance?", "skill": "MySQL", "topic": "DBMS", "difficulty": "MEDIUM"},
            {"question": "Explain the difference between a process and a thread in Operating Systems.", "skill": "Operating Systems", "topic": "Processes", "difficulty": "MEDIUM"},
            {"question": "Design a system that handles 100k concurrent read/write requests. How would you design caching and replication?", "skill": "Algorithms", "topic": "System Design", "difficulty": "HARD"},
            {"question": "What is the time complexity of searching and balancing elements in a Red-Black Tree?", "skill": "Data Structures", "topic": "Trees", "difficulty": "HARD"},
        ]

    def get_initial_question(self, skill: str, topic: str, difficulty: str) -> Dict[str, Any]:
        """
        Retrieves initial question matching characteristics.
        """
        filtered = [q for q in self.question_pool if q["skill"].lower() == skill.lower() or q["difficulty"].upper() == difficulty.upper()]
        if filtered:
            return random.choice(filtered)
        return self.question_pool[0]

    def get_next_adaptive_question(self, last_score: float, current_difficulty: str) -> Dict[str, Any]:
        """
        Adjusts difficulty depending on last evaluated score:
        - Score < 5.0 -> Demote to EASY
        - Score 5.0 - 8.0 -> Keep current_difficulty
        - Score > 8.0 -> Promote to HARD (or keep HARD if already HARD)
        """
        difficulty = current_difficulty.upper()
        if last_score < 5.0:
            difficulty = "EASY"
        elif last_score > 8.0:
            difficulty = "HARD"
            
        filtered = [q for q in self.question_pool if q["difficulty"].upper() == difficulty]
        if not filtered:
            filtered = self.question_pool
            
        return random.choice(filtered)
