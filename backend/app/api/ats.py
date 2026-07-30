
from fastapi import APIRouter,UploadFile,File,Form,HTTPException
from app.services.resume_service import process_resume
from app.ats.jd_parser import parse_jd
from app.services.ats_service import generate_ats_report
from app.services.ai_feedback_service import generate_ai_feedback
from app.models.ats_response import ATSResponse
from app.exceptions.llm_exceptions import LLMAPIError
# import traceback
import logging

logger=logging.getLogger(__name__)
router=APIRouter(
    prefix="/ats",
    tags=["ATS Analysis"]
)




@router.post("/analyze",response_model=ATSResponse)
async def analyze_resume(file: UploadFile=File(...),job_description: str=Form(...)):
    try:

        parsed_resume=process_resume(file)
        parsed_jd=parse_jd(job_description)
        report=generate_ats_report(parsed_resume,parsed_jd)
        try:
            
            logger.info("Ats generated successfully.")
            feedback=generate_ai_feedback(parsed_resume,parsed_jd,report)
        except LLMAPIError:
            feedback={
                "overall_feedback":"AI feedback service is temporarily unavailable.Please try again later.",
                "strengths":[],
                "weaknesses":[],
                "resume_improvements":[],
                "keyword_suggestions":[],
                "missing_skill_suggestions":[],
                "interview_questions":[]
            }
        return {
            **report,
            "ai_feedback":feedback
        }
    except Exception as e:
        logger.exception("unexpected error while analyzing resume.")
        raise HTTPException(
            status_code=500,
            detail="An Unexpected server error occurred."
        )
@router.get("/health")
def ats_health():
    return{
        "message":"ATS API is wokring!"
    }

@router.get("/test")
def test():
    print("TEST HIT")
    return {"status": "ok"}