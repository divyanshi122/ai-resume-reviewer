def get_resume_prompt(resume_text, job_role):
    prompt = f"""
You are an advanced ATS (Applicant Tracking System).

Your task is to evaluate how well this resume matches the job role: "{job_role}".

Follow this process:
1. First, list the 8–12 most important skills, tools, and keywords required for this job role.
2. Then, scan the resume and find which of those skills are present.
3. Penalize the score heavily if many required skills are missing.
4. Be strict. Do not inflate scores.

Resume:
{resume_text}

Return output in this exact format:

Required Skills for {job_role}:
- skill1
- skill2
- ...

Skills Found in Resume:
- skill1
- skill2
- ...

Missing Important Skills:
- skill1
- skill2
- ...

ATS Match Score (0–100):
<number>

Why this score:
<short justification>

3 Resume Improvements:
- rewrite or add bullets to improve match

Final Hiring Decision:
Reject / Consider / Strongly Recommend
"""
    return prompt
