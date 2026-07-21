from app.services.extraction_service import extract_pdf
from app.parser.resume_parser import parse_resume

extracted_data=extract_pdf("test_data/resume-c.pdf")
parsed_data=parse_resume(extracted_data)

print(parsed_data)



