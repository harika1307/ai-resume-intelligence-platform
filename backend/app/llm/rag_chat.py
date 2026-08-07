from app.rag.embedding import EmbeddingService
from app.rag.vector_store import VectorStore
from app.rag.prompt_builder import build_chat_prompt
from app.llm.gemini_client import generate_content
def answer_resume_question(query: str,embedding_service: EmbeddingService,vector_store: VectorStore)->str:
    query_embedding=embedding_service.embed_query(query)
    results=vector_store.search(query_embedding,top_k=3)
    print(results)
    documents = results.get("documents", [[]])[0]
    if not documents:
        return "I couldn't find relevant information in the resume."
    prompt=build_chat_prompt(query,documents)
    return generate_content(prompt)