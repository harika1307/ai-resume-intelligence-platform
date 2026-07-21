from fastapi import APIRouter,UploadFile,File
from app.services.file_services import save_file,validate_file
from app.services.extraction_service import extract_text
from app.parser.resume_parser import parse_resume
router=APIRouter(
    prefix="/resume",
    tags=["Resume"]
)
@router.post("/upload")
async def upload_resume(file: UploadFile=File(...)):
    validate_file(file)
    file_path=save_file(file)
    extracted_data=extract_text(file_path)
    parsed_resume=parse_resume(extracted_data)
    return {
        "message":"Resume uploaded successfully",
        "filename":file_path.name,
        "text":extracted_data
    }

# @router.get("/")
# def resume_home():
#     return {"message":"Resume API is working"}