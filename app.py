from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import random
import PyPDF2
import docx
from resume_parser import ResumeParser
from skill_matcher import SkillMatcher
from text_similarity import TextSimilarity
from authenticity_checker import AuthenticityChecker
from PyPDF2 import PdfReader
import io

app = Flask(__name__, static_folder='static', template_folder='templates')

# Enable CORS for development
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resumes[]' not in request.files:
        return jsonify({'error': 'No files uploaded'}), 400
    
    files = request.files.getlist('resumes[]')
    job_description = request.form.get('job_description', '')
    
    try:
        # For testing purposes, return mock data
        results = []
        for file in files:
            result = {
                'filename': file.filename,
                'match_percentage': random.randint(30, 95),
                'skills_found': ['Python', 'JavaScript', 'React', 'SQL', 'Machine Learning'][:random.randint(2, 5)],
                'experience': ['Software Engineer at Tech Corp', 'Developer at StartUp Inc'],
                'education': ['BS in Computer Science'],
                'contact': {'email': 'candidate@example.com', 'phone': '123-456-7890'}
            }
            results.append(result)
        
        return jsonify(results)
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        return jsonify({'error': 'Analysis failed'}), 500

def extract_text(file):
    text = ""
    file_extension = os.path.splitext(file.filename)[1].lower()
    
    if file_extension == '.pdf':
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    elif file_extension in ['.doc', '.docx']:
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    
    return text

@app.route('/extract_job_description', methods=['POST'])
def extract_job_description():
    if 'job_description_pdf' not in request.files:
        return jsonify({'error': 'No PDF file uploaded'}), 400
    
    pdf_file = request.files['job_description_pdf']
    
    try:
        # Read PDF content
        pdf_reader = PdfReader(io.BytesIO(pdf_file.read()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # Clean and format the extracted text
        text = text.replace('\n', ' ').strip()
        
        return jsonify({
            'extracted_text': text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Ensure the app runs on all network interfaces
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
