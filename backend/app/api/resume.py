from fastapi import APIRouter,UploadFile,File
from app.services.file_services import save_file,validate_file
from app.services.extraction_service import extract_text
router=APIRouter(
    prefix="/resume",
    tags=["Resume"]
)
@router.post("/upload")
async def upload_resume(file: UploadFile=File(...)):
    validate_file(file)
    file_path=save_file(file)
    resume_text=extract_text(file_path)
    return {
        "message":"Resume uploaded successfully",
        "filename":file_path.name,
        "text":resume_text
    }

# @router.get("/")
# def resume_home():
#     return {"message":"Resume API is working"}