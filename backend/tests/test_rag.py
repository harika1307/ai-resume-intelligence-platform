from app.rag.embedding import EmbeddingService
from app.rag.vector_store import VectorStore
from app.rag.ingestion import ingest_resume
from tests.sample_resume import resume_data


embedding_service = EmbeddingService()
vector_store = VectorStore()

# Clear old data before testing
vector_store.reset()

ingest_resume(
    resume_data,
    embedding_service,
    vector_store
)

print("Total chunks stored:", vector_store.count())