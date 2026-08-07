from app.rag.prompt_builder import build_resume_summary_prompt
from app.llm.gemini_client import generate_content

def generate_resume_summary(resume_data: dict)->str:
    prompt=build_resume_summary_prompt(resume_data)
    return generate_content(prompt)
        
    