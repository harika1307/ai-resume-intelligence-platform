from app.prompts.resume_parser_prompt import build_resume_parser_prompt
from app.llm.gemini_client import generate_content
import json
from backend.app.exceptions.llm_exceptions import LLMResponseError
def parse_response(response: str) -> dict:
    try:
        response=response.strip()
        start=response.find("{")
        end=response.rfind("}")
        response=response[start:end+1]
        return json.loads(response)
    except json.JSONDecodeError as e:
        raise LLMResponseError("Invalid JSON returned from Gemini.") from e
def extract_ai_data(resume_text: str)->dict:
    prompt=build_resume_parser_prompt(resume_text)
    raw_response=generate_content(prompt)
    parsed_response=parse_response(raw_response)
    return parsed_response