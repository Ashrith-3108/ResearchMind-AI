from typing import List

import chromadb
from chromadb.config import Settings

from app.config import settings


class VectorService:
    """
    Handles storage and retrieval of vector embeddings.

    Supports:
    - Persistent storage
    - Semantic search
    - RAG
    """

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=settings.VECTOR_DIR,
            settings=Settings(
                anonymized_telemetry=False
            ),
        )

        self.collection = self.client.get_or_create_collection(
            name="researchmind"
        )

    def add_documents(
        self,
        ids: List[str],
        documents: List[str],
        embeddings: List[List[float]],
    ):
        """
        Add documents into the vector database.
        """

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
        )

    def similarity_search(
        self,
        query_embedding: List[float],
        top_k: int = 5,
    ):
        """
        Retrieve most similar chunks.
        """

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

    def count(self):
        """
        Total vectors stored.
        """

        return self.collection.count()

    def delete_all(self):
        """
        Remove all vectors.
        """

        ids = self.collection.get()["ids"]

        if ids:
            self.collection.delete(ids=ids)


vector_service = VectorService()