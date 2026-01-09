import streamlit as st
from groq import Groq
from resume_parser import extract_resume_text
from prompt import get_resume_prompt
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("AI Resume Reviewer")

uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)")

job_role = st.text_input("Enter Job Role (e.g., ML Engineer, VLSI Engineer, Data Analyst)")

st.markdown("### Optional: Paste Job Description")
job_description = st.text_area("If you have a job description, paste it here (optional)")

if st.button("Analyze Resume"):
    if uploaded_file and job_role:
        resume_text = extract_resume_text(uploaded_file)

        # Choose JD or job role
        if job_description.strip() != "":
            context = f"Job Description:\n{job_description}"
        else:
            context = f"Job Role:\n{job_role}"

        prompt = get_resume_prompt(resume_text, context)

        with st.spinner("Analyzing..."):
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )

            result = completion.choices[0].message.content
            st.subheader("AI Analysis")
            st.write(result)
    else:
        st.warning("Please upload a resume and enter job role.")
