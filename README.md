# ATS-Resume-Expert

This  is a Streamlit-based ATS (Applicant Tracking System) Resume Evaluation Tool. It leverages Google Generative AI's Gemini model to provide tailored insights and suggestions on resumes based on a job description. Here’s a detailed explanation:

# Key Features
Job Description Input:

Allows users to input the job description to compare it against the uploaded resume.
Resume Upload:

Accepts resumes in PDF format uploaded by the user.
Uses PyMuPDF (fitz) to extract the first page of the uploaded PDF, converting it into a base64-encoded image to process it with the AI.
Three Functionalities:

Professional Evaluation:
Reviews the resume against the job description.
Provides an evaluation on whether the candidate's profile aligns with the specified role, highlighting strengths and weaknesses.
Skill Improvement Suggestions:
Analyzes skill gaps.
Offers recommendations on areas where the candidate can improve.
Percentage Match:
Calculates a percentage match between the resume and job description.
Identifies missing keywords and provides final thoughts.
AI Model Used:

Google Generative AI (Gemini) is configured via API keys to generate content dynamically based on the inputs provided.
Streamlit User Interface:

Interactive UI for:
Job description entry.
Resume file upload.
Button-based functionality selection.
Outputs results dynamically in the app.
# Workflow
PDF Handling:

Upon uploading a PDF, the first page is extracted and converted into an image format using PyMuPDF.
The image is encoded in Base64 for compatibility with the AI model.
AI-Powered Analysis:

The app queries the Gemini model with:
Job description text.
Extracted PDF content (as an image).
Custom prompts tailored to each button functionality.
Response Display:

Displays results in the Streamlit interface, providing actionable insights based on the AI-generated response.
Prompts Used
Professional Evaluation:

Focuses on HR-style feedback.
Reviews alignment of the resume with the job description.
Highlights strengths and weaknesses.
Skill Improvement Suggestions:

Identifies skill gaps.
Provides guidance for further development to match the role.
Percentage Match:

Calculates how well the resume matches the job description.
Outputs:
Matching percentage.
Missing keywords.
Final thoughts.
# Technologies and Libraries Used
Streamlit:
Framework for building the web-based interface.
PyMuPDF (fitz):
To process PDF files and convert pages into images.
Google Generative AI (Gemini):
For generating tailored responses.
dotenv:
For managing API keys and environment variables.
Base64 Encoding:
To encode images for AI processing.
Usage Scenarios
Job Seekers:
To get feedback on their resumes and identify areas for improvement.
HR Professionals:
To assess resumes and understand their fit for a specific role.
Skill Development:
To receive tailored suggestions on upskilling.
