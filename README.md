# Gemini-Powered ATS Analyzer
ResumeFit AI is an AI-powered Applicant Tracking System (ATS) tool that analyzes how well a resume matches a given job description. It uses Google's Gemini Pro model to evaluate resumes, identify missing keywords, and generate a match score along with a concise profile summary.

## 🚀 Features

- 📄 Upload resume in PDF format
- 📋 Paste job description
- ⚙️ AI-powered analysis using Gemini Pro
- 🧠 Identifies missing but relevant keywords
- 📈 Generates match score (as %)
- 📝 Profile summary extracted using LLM
- 💡 Built with Streamlit for easy UI

## 🧠 How It Works

1. Upload a PDF resume.
2. Paste a job description in the provided text area.
3. Click **Analyze**.
4. Get results like:
   - Resume text preview
   - AI-generated JSON response:
     - `JD Match %`
     - `Missing Keywords`
     - `Profile Summary`

## 🛠️ Tech Stack

- Python 🐍
- Streamlit 🌐
- Google Gemini Pro (via `google.generativeai`)
- PyPDF2 📄
- python-dotenv 🔐
