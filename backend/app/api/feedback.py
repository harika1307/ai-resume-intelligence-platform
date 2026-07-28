from fastapi import APIRouter,UploadFile,File,Form
from app.services.ai_feedback_service import generate_ai_feedback
from app.services.resume_service import process_resume
from app.ats.jd_parser import parse_jd
from app.services.ats_service import generate_ats_report
router=APIRouter(
    prefix="/feedback",
    tags=["AI Feedback"]
)

@router.post("/generate")
async def generate_feedback(file: UploadFile=File(...),job_description: str=Form(...)):
    resume_json=process_resume(file)
    jd_json=parse_jd(job_description)
    ats_report=generate_ats_report(resume_json,jd_json)
    feedback=generate_ai_feedback(resume_json,jd_json,ats_report)
    return feedback