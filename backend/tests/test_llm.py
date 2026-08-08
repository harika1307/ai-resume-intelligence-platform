# from app.llm.resume_summary_generator import generate_resume_summary

# from tests.sample_resume import resume_data

# summary=generate_resume_summary(resume_data)
# print("=" * 60)
# print("RESUME SUMMARY")
# print("=" * 60)
# print(summary)
from app.llm.rag_chat import answer_resume_question
# from app.rag.embedding import EmbeddingService
# from app.rag.vector_store import VectorStore
from app.rag.retriever import Retriever
# embedding_service = EmbeddingService()
# vector_store = VectorStore()

# query = "What projects has the candidate worked on?"
# print("Chunks:", vector_store.count())
# answer = answer_resume_question(
#     query,
#     embedding_service,
#     vector_store
# )

# print("=" * 60)
# print("RESUME CHAT")
# print("=" * 60)
# print(answer)

from app.rag.ingestion import ingest_resume

