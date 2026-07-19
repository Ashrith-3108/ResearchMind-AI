from typing import List

from sentence_transformers import SentenceTransformer

from app.config import settings


class EmbeddingService:
    """
    Generates vector embeddings for research paper chunks.

    Supports:
    - RAG
    - Semantic Search
    - ChromaDB
    - FAISS
    - Pinecone
    """

    def __init__(self):

        self.model = SentenceTransformer(
            settings.EMBEDDING_MODEL
        )

    def embed_text(self, text: str) -> List[float]:
        """
        Generate embedding for a single text.
        """

        embedding = self.model.encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    def embed_documents(
        self,
        documents: List[str],
    ) -> List[List[float]]:
        """
        Generate embeddings for multiple documents.
        """

        embeddings = self.model.encode(
            documents,
            normalize_embeddings=True,
        )

        return embeddings.tolist()

    def embedding_dimension(self) -> int:
        """
        Returns embedding size.
        """

        return self.model.get_sentence_embedding_dimension()


embedding_service = EmbeddingService()