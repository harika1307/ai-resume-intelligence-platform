from app.prompts.jd_prompt import build_jd_prompt
from app.llm.gemini_client import generate_content
from app.parser.ai_parser import parse_response
from app.parser.jd_validator import validate_ai_response
def extract_jd_ai_data(job_description: str)-> dict:
    jd_prompt=build_jd_prompt(job_description)
    raw_response=generate_content(jd_prompt)
    parsed_response=parse_response(raw_response)
    return parsed_response
