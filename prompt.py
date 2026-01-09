def get_resume_prompt(resume_text, job_context):
    prompt = f"""
You are an enterprise-grade Applicant Tracking System (ATS).

You will evaluate a resume against the following job requirement:

{job_context}

Follow these steps carefully.

STEP 1 — Extract skills from the resume:
Extract all technical skills, tools, technologies, and domain keywords from the resume.

STEP 2 — Extract required skills from the job requirement:
From the job role or job description above, extract the most important required skills.

STEP 3 — Compare:
Identify matched and missing skills.

STEP 4 — Score:
Give a strict ATS Match Score (0–100):
- If <40% match → score <40
- If <20% match → score <25
- Only strong match → >70

Resume:
{resume_text}

Return output in this exact format:

ATS Match Score:
<number>

Why this score:
<short explanation>

Resume Skills:
- ...

Required Job Skills:
- ...

Matched Skills:
- ...

Missing Skills:
- ...

3 Resume Improvement Suggestions:
- ...

Final Hiring Decision:
Reject / Consider / Strongly Recommend
"""
    return prompt



