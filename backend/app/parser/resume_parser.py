from app.parser.link_parser import extract_links
from app.parser.contact_parser import extract_email,extract_phone
def parse_resume(extracted_data: dict)->dict:
    """
    Parse extracted resume text and hyperlinks into structured data
    """
    text=extracted_data["text"]
    links=extracted_data["links"]
    return {
        "emails":extract_email(text),
        "phones":extract_phone(text),
        "links":extract_links(links)
    }



def extract_name(text):
    pass




