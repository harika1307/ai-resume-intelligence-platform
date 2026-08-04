import chromadb
import numpy as np
from chromadb.config import Settings
from typing import List,Dict,Any

class VectorStore:
    """
    Handles storing and retrieving document embeddings using ChromaDB.
    """
    def __init__(self):
        self.client=chromadb.PersistentClient(path="chroma_db")
        self.collection=self.client.get_or_create_collection(name="resume_chunks")
    def add_documents(self,ids: List[str],documents: List[str],embeddings: np.ndarray,metadata: List[Dict[str,Any]]):
        """
        Adds documents and their embeddings to vector store.
        """
        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadata
        )
    def search(self,query_embedding: np.ndarray,top_k: int=3):
        results=self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k
        )
        return results
    def count(self)->int:
        """Returns total number of documents in collection."""
        return self.collection.count()
    def reset(self):
        """
        Deletes all documents by recreating collection.
        """
        self.client.delete_collection(name="resume_chunks")
        self.collection=self.client.get_or_create_collection(name="resume_chunks")

    