from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import settings


class ChunkService:
    """
    Service for splitting long research papers into
    semantically meaningful chunks.

    This service is used before:
    - Embedding generation
    - Vector database indexing
    - Retrieval (RAG)
    - Long-document analysis
    """

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                ".",
                "? ",
                "! ",
                " ",
                "",
            ],
            length_function=len,
            is_separator_regex=False,
        )

    def split(self, text: str) -> List[str]:
        """
        Split text into overlapping chunks.
        """

        if not text:
            return []

        return self.splitter.split_text(text)

    def chunk_count(self, text: str) -> int:
        """
        Return total number of chunks.
        """

        return len(self.split(text))

    def preview(self, text: str, limit: int = 3) -> List[str]:
        """
        Preview first few chunks.
        """

        return self.split(text)[:limit]

    def chunk_metadata(self, text: str) -> List[dict]:
        """
        Returns chunks with metadata.
        """

        chunks = self.split(text)

        return [
            {
                "chunk_id": idx,
                "text": chunk,
                "characters": len(chunk),
            }
            for idx, chunk in enumerate(chunks)
        ]

    # ==========================================================
    # NEW
    # ==========================================================

    def get_context(
        self,
        text: str,
        max_chunks: int = 3,
    ) -> str:
        """
        Returns only the first few chunks.

        This dramatically reduces token usage and
        is the first step toward Retrieval-Augmented
        Generation (RAG).
        """

        chunks = self.split(text)

        if not chunks:
            return ""

        return "\n\n".join(chunks[:max_chunks])


chunk_service = ChunkService()