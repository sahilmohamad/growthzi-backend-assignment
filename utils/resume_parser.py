import re
import PyPDF2
import docx

def extract_text_from_pdf(file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(file)
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def parse_resume(file):
    filename = file.filename.lower()
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file)
    elif filename.endswith(".docx") or filename.endswith(".doc"):
        text = extract_text_from_docx(file)
    else:
        return {"error": "Unsupported file format"}

  
    name_match = re.search(r"Name[:\-]?\s*(.*)", text, re.IGNORECASE)
    name = name_match.group(1).strip() if name_match else "Unknown"

    skills_match = re.findall(r"(Python|Flask|Django|SQL|Java|C\+\+)", text, re.IGNORECASE)
    skills = list(set([s.capitalize() for s in skills_match])) if skills_match else []

    education = []
    if "BCA" in text.upper():
        education.append("Bachelor of Computer Applications")
    if "MCA" in text.upper():
        education.append("Master of Computer Applications")

    experience = []
    if "intern" in text.lower():
        experience.append("Internship Experience")
    if "developer" in text.lower():
        experience.append("Developer Role")

    data = {
        "hero": {"name": name, "bio": "Aspiring software engineer"},
        "about": {"summary": "Auto-generated from resume"},
        "skills": skills,
        "experience": experience,
        "education": education,
        "contact": {"email": "sample@email.com"}  
    }

    return data
