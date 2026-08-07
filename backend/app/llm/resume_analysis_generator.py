from app.rag.prompt_builder import build_resume_analysis_prompt
from app.llm.gemini_client import generate_content

def generate_resume_analysis(resume_data: dict,ats_score: dict)->str:
    prompt=build_resume_analysis_prompt(resume_data,ats_score)
    return generate_content(prompt)