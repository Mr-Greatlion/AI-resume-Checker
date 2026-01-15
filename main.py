from parser.ocr_engine import pdf_to_text
from parser.extractor import extract_email, extract_phone, extract_name, extract_education
from parser.experience_calc import calculate_experience

resume_path = "data/sample_resume.pdf"

text = pdf_to_text(resume_path)

result = {
    "name": extract_name(text),
    "email": extract_email(text),
    "phone": extract_phone(text),
    "education": extract_education(text),
    "experience_years": calculate_experience(text)
}

print("\n📄 EXTRACTED DATA\n")
for k, v in result.items():
    print(f"{k}: {v}")
