
from fastapi import APIRouter,UploadFile,File,Form,HTTPException
from app.services.resume_service import process_resume
from app.ats.jd_parser import parse_jd
from app.services.ats_service import generate_ats_report
import traceback
router=APIRouter(
    prefix="/ats",
    tags=["ATS Analysis"]
)
@router.post("/analyze")
async def analyze_resume(file: UploadFile=File(...),job_description: str=Form(...)):
    try:
        parsed_resume=process_resume(file)
        print("Resume processed")
        parsed_jd=parse_jd(job_description)
        print("JD proceessed")
        report=generate_ats_report(parsed_resume,parsed_jd)
        print("Ats generated.")
        return report
    except Exception as e:
        traceback.print_exc()
        raise

@router.get("/health")
def ats_health():
    return{
        "message":"ATS API is wokring!"
    }