from app.llm.resume_summary_generator import generate_resume_summary

from tests.sample_resume import resume_data

summary=generate_resume_summary(resume_data)
print(summary)