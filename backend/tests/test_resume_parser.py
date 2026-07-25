from app.services.extraction_service import extract_pdf
from app.parser.resume_parser import parse_resume
import json
pdf_path="tests/data/resume-c.pdf"

pdf_data=extract_pdf(pdf_path)

resume_data=parse_resume(
    text=pdf_data["text"],
    links=pdf_data["links"]
)
with open("tests/output.json","w",encoding="utf-8") as f:
    json.dump(resume_data,f,indent=4,ensure_ascii=False)
print(json.dumps(resume_data,indent=4))