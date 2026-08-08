import numpy as np
from app.rag.embedding import EmbeddingService
from app.rag.vector_store import VectorStore
from app.rag.chunking import Chunker
def ingest_resume(resume_data: str,embedding_service: EmbeddingService,vector_store: VectorStore):
    chunks=Chunker.chunk_text(resume_data)
    embeddings=embedding_service.embed_chunks(chunks)
    ids=[f"resume_chunk_{i}" for i in range(len(chunks))]
    vector_store.add_documents(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadata=[
            {"source":"resume"}
            for _ in chunks
        ]
    )