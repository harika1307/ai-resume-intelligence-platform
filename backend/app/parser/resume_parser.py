from app.parser.link_parser import extract_links
from app.parser.contact_parser import extract_email,extract_phone
from app.parser.ai_parser import extract_ai_data
from app.parser.name_parser import extract_name
def parse_resume(text: str,links: list)->dict:
    """
    Parse extracted resume text and hyperlinks into structured data
    """
    
    ai_data=extract_ai_data(text)
    link_data=extract_links(links)
    return {
        "name":extract_name(text),
        "emails":extract_email(text),
        "phones":extract_phone(text),
        **link_data,
        **ai_data,
    }



