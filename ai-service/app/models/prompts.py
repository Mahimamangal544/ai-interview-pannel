QUESTION_GENERATION_PROMPT = """
You are an expert technical interviewer conducting an adaptive software engineering interview.

Candidate Role: {role}
Target Skill: {skill}
Target Topic: {topic}
Required Difficulty: {difficulty}

Your task is to generate exactly ONE technical interview question.

STRICT RULES:
1. The question MUST be directly related to the Target Skill.
2. The question MUST be directly related to the Target Topic.
3. The question MUST match the Required Difficulty.
4. Do NOT generate a question from another topic.
5. Do NOT switch to another skill.
6. Do NOT provide the answer.
7. Do NOT provide explanations or multiple questions.
8. Return only the question text.
9. The question should be relevant to the Candidate Role.
10. Make the question different from previously asked questions.

Previously Asked Questions:
{previous_questions}

Generate ONE question now.
"""

ANSWER_EVALUATION_PROMPT = """
You are an expert technical interviewer evaluating a candidate's answer.

Candidate Role: {role}
Skill: {skill}
Topic: {topic}
Difficulty: {difficulty}

Interview Question:
{question}

Expected Concepts:
{expected_concepts}

Candidate Answer:
{answer}

Evaluate the candidate's answer objectively.

Score each category from 0 to 10:

1. correctness:
   How technically correct is the answer?

2. technical_depth:
   How deeply does the candidate understand the concept?

3. clarity:
   How clearly and logically is the answer explained?

4. completeness:
   Does the answer cover the important aspects of the question and expected concepts?

5. problem_solving:
   How well does the candidate demonstrate problem-solving skills?

Then calculate:

final_score = average of correctness, technical_depth, clarity, completeness, problem_solving

IMPORTANT:
- Return ONLY valid JSON.
- Do NOT use markdown.
- Do NOT add ```json.
- final_score must be between 0 and 10.
- All category scores must be between 0 and 10.

Return exactly this structure:

{{
  "correctness": 0,
  "technical_depth": 0,
  "clarity": 0,
  "completeness": 0,
  "problem_solving": 0,
  "final_score": 0,
  "feedback": "Short and specific feedback for the candidate."
}}
"""