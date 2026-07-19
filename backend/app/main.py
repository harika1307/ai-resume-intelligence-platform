from fastapi import FastAPI
from app.database.database import db
from app.api.resume import router as resume_router


app=FastAPI()
app.include_router(resume_router)

@app.on_event("startup")
async def startup_db():
    try:
        db.list_collection_names()
        print("Connected to Mongodb successfully!")
    except Exception as e:
        print(f"Mongodb connection failed:{e}")

@app.get("/")
def home():
    return {"message":"Welcome to AI Resume Intelligence platform"}