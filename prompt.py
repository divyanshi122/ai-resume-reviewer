def get_resume_prompt(resume_text, job_role):
    prompt = f"""
You are an enterprise-grade Applicant Tracking System (ATS).

Follow these steps carefully.

STEP 1 — Extract skills from the resume:
From the resume below, extract all technical skills, tools, technologies, and domain keywords as a clean bullet list.

STEP 2 — Extract skills for the job role:
List the 8–12 most important skills required for the job role: "{job_role}".

STEP 3 — Compare:
Compare both lists and determine:
- Matching skills
- Missing skills

STEP 4 — Score:
Give a strict ATS Match Score from 0 to 100:
- If fewer than 40% of required skills are found → score below 40
- If fewer than 20% are found → score below 25
- Only give >70 if strong match

Resume:
{resume_text}

Return output in this exact format:

ATS Match Score:
<number>

Why this score:
<short explanation>

Resume Skills:
- ...

Required Skills for {job_role}:
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


