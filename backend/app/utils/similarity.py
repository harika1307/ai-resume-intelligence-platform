import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
def get_similarity_score(embedding1: np.ndarray,embedding2: np.ndarray)->float:
    similarity=cosine_similarity(
        embedding1.reshape(1,-1),embedding2.reshape(1,-1)
    )
    return similarity.item()