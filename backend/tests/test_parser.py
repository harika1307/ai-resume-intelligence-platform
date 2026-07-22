# from app.services.extraction_service import extract_pdf
# from app.parser.resume_parser import parse_resume

# extracted_data=extract_pdf("test_data/resume-c.pdf")
# parsed_data=parse_resume(extracted_data)

# print(parsed_data)

from app.parser.name_parser import extract_name
with open("tests/data/test_resume.txt","r",encoding="utf-8") as f:
    text=f.read()

name = extract_name(text)

print("=" * 40)
print("Extracted Name")
print("=" * 40)
print(name)

