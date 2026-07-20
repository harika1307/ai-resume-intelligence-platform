from pathlib import Path
import shutil
import uuid
from fastapi import UploadFile,HTTPException
from app.core.constants import MAX_FILE_SIZE,ALLOWED_TYPES


UPLOAD_DIR=Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

def save_file(file:UploadFile):
    unique_filename=f"{uuid.uuid4()}_{file.filename}"
    file_path=UPLOAD_DIR/unique_filename
    with open (file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    return file_path



def validate_file(file:UploadFile):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400,detail="Only PDF and DOCX files are allowed")
    try:
        file.file.seek(0,2) #move pointer to end
        size=file.file.tell()
        if size==0:
            raise HTTPException(status_code=400,detail="Uploaded file is empty")
        elif size>MAX_FILE_SIZE:
            raise HTTPException(status_code=400,detail="Maximum allowed file size is 5MB")
    finally:
        file.file.seek(0)