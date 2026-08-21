# AI Prompt templates for evaluations and question generation

QUESTION_GENERATION_PROMPT = """
You are an expert interviewer. Generate a technical question for a software developer candidate.
Target Skill: {skill}
Topic: {topic}
Difficulty: {difficulty}

Generate a clear, standalone question. Do not provide the answer.
"""

ANSWER_EVALUATION_PROMPT = """
You are an expert technical evaluator. Evaluate the candidate's answer based on the following context.
Question: {question_text}
Candidate's Answer: {answer_text}

Rate each of the following metrics on a scale of 0 to 10:
1. Correctness (Is the code/concept accurate?)
2. Technical Depth (Does it demonstrate senior/architectural understanding?)
3. Clarity (Is it easy to follow?)
4. Completeness (Are edge cases addressed?)

Provide your response in JSON format containing "correctness", "technical_depth", "clarity", "completeness", "final_score", and "feedback".
"""
