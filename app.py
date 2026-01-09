import streamlit as st
from groq import Groq
from resume_parser import extract_resume_text
from prompt import get_resume_prompt
import os

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------------- UI ----------------

st.title("AI Resume Reviewer")
st.markdown("**Fields marked with * are required**")

# Resume Upload
resume_file = st.file_uploader("Upload your resume * (PDF or DOCX)", type=["pdf", "docx"])

# Job Role (Required)
job_role = st.text_input("Job Role * (e.g., ML Engineer, VLSI Engineer, Data Analyst)")

st.markdown("### Job Description")

# JD Paste (Optional)
jd_text = st.text_area("Paste job description")

# JD Upload (Optional)
jd_file = st.file_uploader("Or upload job description (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])


# ---------------- Helper ----------------

def extract_jd_text(file):
    if file is None:
        return ""
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        return extract_resume_text(file)


# ---------------- Analyze ----------------

if st.button("Analyze Resume"):
    if resume_file and job_role:
        resume_text = extract_resume_text(resume_file)

        # Get JD content if provided
        jd_content = ""
        if jd_file:
            jd_content = extract_jd_text(jd_file)
        elif jd_text.strip() != "":
            jd_content = jd_text

        # Choose context: JD > Job Role
        if jd_content.strip() != "":
            context = f"Job Description:\n{jd_content}"
        else:
            context = f"Job Role:\n{job_role}"

        prompt = get_resume_prompt(resume_text, context)

        with st.spinner("Analyzing..."):
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            result = completion.choices[0].message.content

            st.subheader("AI Analysis")
            st.write(result)

    else:
        st.warning("Please upload a resume and enter the job role.")
