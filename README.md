# Growthzi Backend Developer Assignment

# Overview :
This project implements the required backend APIs for the Growthzi Backend Developer Assignment:

1. **Portfolio Website Generation from Resume (PDF/DOC)**
   - Upload a resume file (PDF/DOC).  
   - Parse user details (name, skills, experience, education).  
   - Return structured JSON that can be used for a portfolio website.  

2. **Multi-Lingual Website Support**  
   - Accept text + target language code.  
   - Return translated version of the text.  

3. **Multi-Currency Pricing Display**  
   - Accept a country code.  
   - Return product pricing in the local currency (mock conversion rates).  

4. **Frontend Integration (HTML + JS + CSS)**  
   - A simple testing UI is included under `templates/index.html` to interact with APIs.  


## Tech Stack :
- **Backend**: Python, Flask, Flask-CORS  
- **Resume Parsing**: PyPDF2, python-docx  
- **Translation**: googletrans  
- **Frontend**: HTML, CSS, JavaScript  


## Setup Instructions :

### 1. Clone Repository
```bash
git clone https://github.com/sahilmohamad/growthzi-backend-assignment.git
cd growthzi-backend-assignment

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux

3. Install Dependencies
pip install -r requirements.txt

4. Run the Application
python app.py

Server will start at:
Link - http://127.0.0.1:5000/


API Endpoints
1. Resume → Portfolio
POST /api/portfolio
Upload file in form-data (key = file).

Example Response:
{
  "hero": {"name": "Sahil", "bio": "Aspiring software engineer"},
  "about": {"summary": "Auto-generated from resume"},
  "skills": ["Python", "Flask", "SQL"],
  "experience": ["Developer Role"],
  "education": ["Bachelor of Computer Applications", "Master of Computer Applications"],
  "contact": {"email": "sample@email.com"}
}

2. Translation
POST /api/translate
Body (JSON):
{
  "text": "Hello, welcome to my portfolio website",
  "lang": "hi"
}

Response:
{
  "original_text": "Hello, welcome to my portfolio website",
  "translated_text": "नमस्ते, मेरी पोर्टफोलियो वेबसाइट पर आपका स्वागत है",
  "target_lang": "hi"
}

3. Pricing
GET /api/pricing?country=IN
Response:
{
  "product": "Pro Plan",
  "price_usd": "$10",
  "price_local": "₹800.00",
  "currency": "IN"
}

Frontend
A simple HTML + JS + CSS frontend is provided at /templates/index.html to test APIs in the browser.
Run the Flask server and open:
Link : http://127.0.0.1:5000/

Demo Video:
Link - https://drive.google.com/file/d/1sUMEkiXPTsYezv6SGe7PQYwbEo2-U1zj/view?usp=sharing

📂 Project Structure
growthzi_backend_assignment/
│── app.py
│── routes/
│   ├── portfolio.py
│   ├── translate.py
│   ├── pricing.py
│── utils/
│   ├── resume_parser.py
│   ├── currency.py
│── templates/
│   └── index.html
│── static/
│   ├── script.js
│   └── style.css
│── requirements.txt
│── README.md
