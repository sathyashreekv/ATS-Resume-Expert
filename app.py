
from dotenv import load_dotenv
import streamlit as st
import os
import io
import fitz  # PyMuPDF for handling PDFs
import base64

# Load environment variables
load_dotenv()
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Open the uploaded PDF with PyMuPDF (Fitz)
        pdf_document = uploaded_file.read()
        doc = fitz.open(stream=pdf_document, filetype="pdf")
        
        # Extract the first page as an image
        first_page = doc.load_page(0)  # Load the first page
        pix = first_page.get_pixmap()   # Convert page to an image
        
        # Convert the image to bytes for further processing
        img_byte_arr = io.BytesIO(pix.tobytes("jpeg"))
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # Encode the image in base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System ")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF uploaded successfully")

submit1 = st.button("Tell me About the Resume")
submit2 = st.button("How can I Improve my Skills")
submit3 = st.button("Percentage match")

input_prompt1 = """You are an experienced HR with Tech experience in the field of Data Science, Full stack, web development, Big Data Engineering, DEVOPS, Data Analytics. Your task is to review the provided resume against the job description for these profiles.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job description."""

input_prompt2 = """You are a career coach with expertise in fields like Data Science, Full Stack Development, Big Data Engineering, DevOps, and Data Analytics.
Please review the provided resume against the job description and suggest areas for improvement in skills or knowledge.
Your feedback should focus on gaps in the candidate's current skill set and provide recommendations on how they can improve in order to better match the job description."""


input_prompt3 = """You are a Skilled ATS (Application Tracking System) scanner with a deep understanding of Data Science, Full stack, web development, Big Data Engineering, DEVOPS, Data Analytics, and deep ATS functionality.
Your task is to evaluate the resume against the provided job description. Give me the percentage match if the resume matches the job description. First the output should come as a percentage and then keywords missing, and last final thoughts."""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The response is")
        st.write(response)
    else:
        st.write("Please upload the resume")
elif submit2:
       if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("Skill Improvement Suggestions")
        st.write(response)
       else:
         st.write("Please upload the resume")   

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The response is")
        st.write(response)
