import re
def extract_email(text: str)->list[str]:
    pattern=r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    all_emails=re.findall(pattern,text)
    return all_emails

def extract_phone(text: str)->list[str]:
    pattern=r"(?:\(\+91\)|\+91|91)?[ -]?[0-9]{10}"
    phones=re.findall(pattern,text)
    return phones