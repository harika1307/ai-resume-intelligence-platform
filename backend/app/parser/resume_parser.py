import re
def parse_resume(text):
    return {
        "emails":extract_email(text),
        "phones":extract_phone(text)
    }

def extract_email(text):
    pattern=r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    all_emails=re.findall(pattern,text)
    return all_emails

def extract_phone(text):
    pattern=r"(?:\(\+91\)|\+91|91)?[ -]?[0-9]{10}"
    phones=re.findall(pattern,text)
    return phones
def extract_links(text):
    pass
def extract_name(text):
    pass

