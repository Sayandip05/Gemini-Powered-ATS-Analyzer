import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response
def get_gemini_response(input_text):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(input_text)
        return response.text
    except Exception as e:
        return f"Error while generating response: {str(e)}"

# Function to extract text from PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

# Prompt Template
input_prompt = """
You are an expert Applicant Tracking System (ATS) with deep domain knowledge in software engineering, data science, data analytics, and big data engineering roles.

Your tasks:
1. Analyze the resume against the provided job description.
2. Evaluate how well the resume matches the job.
3. Identify missing but relevant keywords that would strengthen the resume.
4. Provide a concise profile summary based on the resume content.
5. Assign a percentage score indicating the match between the resume and job description.

Make sure the evaluation is strict, considering the current competitive job market.

Return the result strictly in this JSON format:
{{
  "JD Match": "XX%",
  "MissingKeywords": ["keyword1", "keyword2", ...],
  "ProfileSummary": "Concise summary here"
}}

Resume:
{text}

Job Description:
{jd}
"""

# Streamlit UI
st.set_page_config(page_title="Smart ATS Resume Checker", layout="centered")
st.title("📄 Smart ATS")
st.write("Upload your resume and paste a job description to see how well it matches!")

# Input
jd = st.text_area("📋 Paste the Job Description", height=200)
uploaded_file = st.file_uploader("📁 Upload Your Resume (PDF only)", type="pdf")

# Submit button
if st.button("🔍 Analyze"):
    if uploaded_file and jd.strip():
        with st.spinner("Reading and analyzing..."):
            resume_text = input_pdf_text(uploaded_file)
            prompt = input_prompt.format(text=resume_text, jd=jd)
            result = get_gemini_response(prompt)

        st.subheader("📑 Resume Extracted Text:")
        st.write(resume_text)

        st.subheader("📊 Gemini Evaluation:")
        st.code(result, language="json")
    else:
        st.warning("Please upload a PDF file and enter a job description.")
