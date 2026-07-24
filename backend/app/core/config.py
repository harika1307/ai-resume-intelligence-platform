from dotenv import load_dotenv
import os
load_dotenv()
MONGODB_URL=os.getenv("MONGODB_URL")
DATABASE_NAME=os.getenv("DATABASE_NAME")
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
MODEL_NAME=os.getenv("MODEL_NAME","gemini-3.5-flash")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing.Please check your .env file.")
