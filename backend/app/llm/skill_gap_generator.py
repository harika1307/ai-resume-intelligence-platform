from app.rag.prompt_builder import build_skill_gap_prompt
from app.llm.gemini_client import generate_content

def generate_skill_gap(resume_data: dict,jd_data: dict)->str:
    prompt=build_skill_gap_prompt(resume_data,jd_data)
    return generate_content(prompt)