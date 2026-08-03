from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer
class EmbeddingService:
    def __init__(self):

        self.model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    def embed_text(self,text: str)->np.ndarray:
        """
        Generates an embedding vector for a single text.
        Args:
            text: Input text.
        Returns:
            Embedding vector.
        """
        if not text.strip():
            return []
        embedding=self.model.encode(text,convert_to_numpy=True)
        return embedding
    def embed_chunks(self,chunks: List[str])->np.ndarray:
        """
        Generates embeddings for multiple text chunks.
        Args:
            chunks: List of text chunks.
        Returns:
            NumPy array of embeddings.
        """
        if not chunks:
            return np.array([])
        embeddings=self.model.encode(chunks,convert_to_numpy=True)
        return embeddings
        
        
        
        
    def embed_query(self,query: str)->np.ndarray:
        if not query:
            return np.array([])
        embedding=self.embed_text(query)
        return embedding