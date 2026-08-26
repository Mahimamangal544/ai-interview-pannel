from typing import Dict, List, Any


class EvaluationStore:

    def __init__(self):
        # interview_id -> list of evaluated answers
        self._evaluations: Dict[int, List[Dict[str, Any]]] = {}

    def add_evaluation(
        self,
        interview_id: int,
        question_id: int,
        question_text: str,
        skill: str,
        evaluation: Dict[str, Any]
    ):

        if interview_id not in self._evaluations:
            self._evaluations[interview_id] = []

        record = {
            "question_id": question_id,
            "question_text": question_text,
            "skill": skill,

            "correctness": evaluation.get("correctness", 0),
            "technical_depth": evaluation.get("technical_depth", 0),
            "clarity": evaluation.get("clarity", 0),
            "completeness": evaluation.get("completeness", 0),
            "final_score": evaluation.get("final_score", 0),
            "feedback": evaluation.get("feedback", "")
        }

        self._evaluations[interview_id].append(record)

    def get_evaluations(
        self,
        interview_id: int
    ) -> List[Dict[str, Any]]:

        return self._evaluations.get(interview_id, [])

    def clear_interview(
        self,
        interview_id: int
    ):

        if interview_id in self._evaluations:
            del self._evaluations[interview_id]


# Single shared instance
evaluation_store = EvaluationStore()