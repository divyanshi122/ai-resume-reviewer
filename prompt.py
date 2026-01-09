def get_resume_prompt(resume_text, job_role):
    prompt = f"""
You are a strict Applicant Tracking System (ATS) used by top tech companies.

Your job is to evaluate how well this resume matches the job role: {job_role}

You MUST follow these rules:
- If core skills for the role are missing, the ATS score MUST be below 50
- If most required skills are missing, the score MUST be below 30
- Only give scores above 70 if the resume strongly matches the role
- Do NOT be generous

For Machine Learning / AI roles, important skills include:
Python, Machine Learning, Deep Learning, Data Science, Neural Networks, PyTorch, TensorFlow, Scikit-Learn, AI projects, model training, evaluation.

Resume:
{resume_text}

Return the result strictly in this format:

ATS Score: <number between 0 and 100>

Missing or Weak Skills:
- List missing important skills

Strong Skills:
- List strong matching skills

Why this ATS Score:
- Give short justification

3 Improved Resume Bullet Points:
- Rewrite weak bullets to better match the role

Final Hiring Recommendation:
- Reject / Consider / Strongly Recommend with reason
"""
    return prompt
