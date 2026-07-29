from app.services.file_services import save_file,validate_file
from app.services.extraction_service import extract_text,extract_pdf_links
from app.parser.resume_parser import parse_resume

def process_resume(file):
    """Validate,save,extract and parse an uploaded resume.
    Returns structured resume JSON.
    """
   
    validate_file(file)
    print("2")
    file_path=save_file(file)
    print("3")
    resume_text=extract_text(file_path)
    print("4")
    resume_links=extract_pdf_links(file_path)
    print("5")
    parsed_resume=parse_resume(resume_text,resume_links)
    print("6")
    return parsed_resume