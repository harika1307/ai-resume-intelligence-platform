from app.rag.prompt_builder import build_interview_prompt
from app.llm.gemini_client import generate_content

def generate_interview_questions(resume_data: dict,jd_data: dict)->str:
    prompt=build_interview_prompt(resume_data,jd_data)
    return generate_content(prompt)