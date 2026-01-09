import streamlit as st
from groq import Groq
from resume_parser import extract_resume_text
from prompt import get_resume_prompt
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("AI Resume Reviewer")

uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)")
job_role = st.text_input("Enter the job role (e.g., Data Scientist, ML Engineer)")

if st.button("Analyze Resume"):
    if uploaded_file and job_role:
        resume_text = extract_resume_text(uploaded_file)
        prompt = get_resume_prompt(resume_text, job_role)

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
        st.warning("Please upload a resume and enter job role.")


