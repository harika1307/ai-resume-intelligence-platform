import json
from app.prompts.feedback_prompt import build_feedback_prompt
from app.llm.gemini_client import generate_content
from app.parser.ai_parser import parse_response
from app.exceptions.llm_exceptions import LLMAPIError
def generate_ai_feedback(resume_json: dict,jd_json: dict,ats_report: dict):
    try:
        prompt=build_feedback_prompt(resume_json,jd_json,ats_report)
        raw_response=generate_content(prompt)
        feedback=parse_response(raw_response)
        return feedback
    except LLMAPIError:
        raise