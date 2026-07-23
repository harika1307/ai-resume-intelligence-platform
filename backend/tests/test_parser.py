# from app.services.extraction_service import extract_pdf
# from app.parser.resume_parser import parse_resume

# extracted_data=extract_pdf("test_data/resume-c.pdf")
# parsed_data=parse_resume(extracted_data)

# print(parsed_data)

from app.parser.name_parser import extract_name,extract_name_heuristic,extract_name_spacy
with open("tests/data/test_resume.txt","r",encoding="utf-8") as f:
    text=f.read()

print("=" * 40)
print("Heuristic")
print(extract_name_heuristic(text))

print("=" * 40)
print("spaCy")
print(extract_name_spacy(text))

print("=" * 40)
print("Final")
print(extract_name(text))

