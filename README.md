## Multi-functional Question Generator App

An interactive, AI-powered Question Generator web application that automatically generates **MCQs, Fill-in-the-Blanks, and True/False questions** from text or PDF study materials.  
Built with **Python, Flask, and Machine Learning (TF-IDF)** and designed with a **Modern glassmorphism UI**.

---

## Features:

### AI & ML Features
- Automatic **question generation** using TF-IDF keyword extraction
- Supports **multiple question types**:
  - Multiple Choice Questions (MCQ)
  - Fill in the Blanks
  - True / False
- **Difficulty levels**: Easy, Medium, Hard
- Duplicate question avoidance

### User Experience
- Modern **glassmorphism UI**
- Tab-based input (Text / PDF)
- Interactive answer **Show / Hide toggle**
- Smooth animations & responsive layout
- Clean and distraction-free design

### Input Support
- Paste text directly
- Upload PDF files
- Choose number of questions dynamically

---

## Tech Stack

| Category | Technology |
|--------|-----------|
| Backend | Python, Flask |
| Machine Learning | TF-IDF (Scikit-learn) |
| Frontend | HTML, CSS, JavaScript |
| PDF Processing | PyPDF2 |
| IDE | VS Code |

---

## Project Structure:

smart-question-generator/
│
├── app.py
├── requirements.txt
│
├── ml/
│ └── keyword_extractor.py
│
├── services/
│ ├── text_service.py
│ ├── question_service.py
│ └── difficulty_service.py
│
├── templates/
│ ├── index.html
│ └── result.html
│
└── static/
├── style.css
└── script.js


## Installation & Setup (VS Code):

1️⃣ Clone the Repository
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Application
python app.py
5️⃣ Open in Browser
http://127.0.0.1:5000

## How It Works:
User provides text or PDF

Text is cleaned and split into sentences

TF-IDF extracts important keywords

Keywords are replaced to form questions

Output is displayed with interactive controls

## Use Cases:
Students preparing for exams

Teachers generating quizzes

E-learning platforms

Interview & test preparation

Academic research / final-year projects

## Future Enhancements:
 User authentication & question history

 Export questions as PDF / DOCX

 LLM integration (GPT / LLaMA)

 Dark / Light mode toggle

 Analytics dashboard

 FastAPI REST API

## Author:
Md. Habibur Rahman
B.Sc. in Computer Science & Engineering
Dhaka University of Engineering & Technology (DUET), Gazipur

