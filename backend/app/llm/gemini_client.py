from google import genai
from app.core.config import GOOGLE_API_KEY,MODEL_NAME
from backend.app.exceptions.llm_exceptions import LLMAPIError
client=genai.Client(api_key=GOOGLE_API_KEY)

def generate_content(prompt: str)->str:
    try:
        response=client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )
        return response.text
    except Exception as e:
        raise LLMAPIError(str(e)) from e