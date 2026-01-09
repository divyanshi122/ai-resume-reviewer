def get_resume_prompt(resume_text, job_role):
    prompt = f"""
You are an expert ATS (Applicant Tracking System) and professional recruiter.

Analyze the following resume for the job role: {job_role}

Resume:
{resume_text}

Give the output in the following format:

ATS Score: (out of 100)

Grammar and Formatting Issues:
- List mistakes

Skill Gaps:
- List missing or weak skills for the given role

Improved Resume Bullet Points:
- Rewrite 3 important bullets to be more professional and impactful

Final Hiring Recommendation:
- Should this candidate be shortlisted? Yes or No with reason
"""
    return prompt
