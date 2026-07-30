from fastapi import FastAPI
from app.database.database import db
from app.api.resume import router as resume_router
from app.api.ats import router as ats_router
from app.api.feedback import router as feedback_router
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume_router)
app.include_router(ats_router)
app.include_router(feedback_router)



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