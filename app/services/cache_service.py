import hashlib
import json
from pathlib import Path
from typing import Any, Optional

from app.config import settings


class CacheService:
    """
    Simple file-based cache.

    Stores:
    - LLM responses
    - Analysis
    - Summaries
    - Embeddings metadata

    Future:
    Redis can replace this without changing agents.
    """

    def __init__(self):

        self.cache_dir = Path(settings.CACHE_DIR)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _hash(self, text: str) -> str:
        """
        Generate SHA256 hash.
        """

        return hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

    def exists(self, key: str) -> bool:

        file = self.cache_dir / f"{self._hash(key)}.json"

        return file.exists()

    def get(self, key: str) -> Optional[Any]:

        file = self.cache_dir / f"{self._hash(key)}.json"

        if not file.exists():
            return None

        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)

    def set(self, key: str, value: Any):

        file = self.cache_dir / f"{self._hash(key)}.json"

        with open(file, "w", encoding="utf-8") as f:
            json.dump(
                value,
                f,
                indent=4,
                ensure_ascii=False,
            )

    def clear(self):

        for file in self.cache_dir.glob("*.json"):
            file.unlink()


cache_service = CacheService()