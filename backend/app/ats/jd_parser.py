
from app.ats.jd_ai_parser import extract_jd_ai_data
from app.parser.jd_validator import validate_ai_response
def parse_jd(job_description: str)->dict:
    """
    Parse extracted job description skills into structured data
    """
    ai_data=extract_jd_ai_data(job_description)
    validated_data=validate_ai_response(ai_data)
    return validated_data