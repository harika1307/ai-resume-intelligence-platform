# from app.rag.embedding import EmbeddingService
# from app.rag.vector_store import VectorStore
from app.rag.prompt_builder import build_chat_prompt
from app.llm.gemini_client import generate_content
from app.rag.retriever import Retriever
def answer_resume_question(query: str,retriever: Retriever)->str:
   
    results=retriever.retrieve(query,top_k=3)
    # print(results)
    documents = results.get("documents", [[]])[0]
    if not documents:
        return "I couldn't find relevant information in the resume."
    # print("Chunks:", vector_store.count())
    prompt=build_chat_prompt(query,documents)
    return generate_content(prompt)