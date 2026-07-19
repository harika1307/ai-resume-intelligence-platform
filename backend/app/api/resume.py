from fastapi import APIRouter,UploadFile,File
from app.services.file_services import save_file,validate_file

router=APIRouter(
    prefix="/resume",
    tags=["Resume"]
)
@router.post("/upload")
async def upload_resume(file: UploadFile=File(...)):
    validate_file(file)
    filename=save_file(file)
    return {
        "message":"Resume uploaded successfully",
        "filename":filename
    }

# @router.get("/")
# def resume_home():
#     return {"message":"Resume API is working"}