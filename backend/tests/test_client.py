# from google import genai
from app.core.config import GOOGLE_API_KEY
# client=genai.Client(api_key=GOOGLE_API_KEY)

# for model in client.models.list():
#     print(model.name)


# from app.llm.gemini_client import generate_content
# response=generate_content(
#     "Reply with exactly one word: SUCCESS"
# )
# print(response)

# from app.core.config import GOOGLE_API_KEY
# from google import genai

# from google import genai

# API_KEY = GOOGLE_API_KEY

# client = genai.Client(api_key=API_KEY)

# response = client.models.generate_content(
#     model="gemini-3.5-flash",
#     contents="Say hello"
# )

# print(response.text)



# client = genai.Client(api_key=GOOGLE_API_KEY)

# response = client.models.generate_content(
#     model="gemini-3.5-flash",
#     contents="Reply with only the word SUCCESS"
# )

# print(response.text)