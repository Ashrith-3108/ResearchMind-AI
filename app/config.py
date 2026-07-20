from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global project configuration.

    Automatically loads variables from .env
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    # ============================
    # LLM
    # ============================

    OPENROUTER_API_KEY: str

    MODEL_NAME: str = "openai/gpt-4.1"

    TEMPERATURE: float = 0.0

    MAX_TOKENS: int = 1024

    # ============================
    # Project
    # ============================

    PROJECT_NAME: str = "ResearchMind AI"

    VERSION: str = "1.0.0"

    DEBUG: bool = True

    # ============================
    # Directories
    # ============================

    OUTPUT_DIR: str = "outputs"

    REPORT_DIR: str = "outputs/reports"

    JSON_DIR: str = "outputs/json"

    MARKDOWN_DIR: str = "outputs/markdown"

    PDF_DIR: str = "outputs/pdf"

    LOG_DIR: str = "app/storage/logs"

    CACHE_DIR: str = "app/storage/cache"

    VECTOR_DIR: str = "app/storage/embeddings"

    # ============================
    # Embeddings
    # ============================

    EMBEDDING_MODEL: str = "BAAI/bge-small-en-v1.5"

    # ============================
    # Chunking
    # ============================

    CHUNK_SIZE: int = 1200

    CHUNK_OVERLAP: int = 250

    # ============================
    # Retry Settings
    # ============================

    MAX_RETRIES: int = 2
    # ============================
    # File Upload
    # ============================

    MAX_FILE_SIZE_MB: int = 50

    # ============================
    # Confidence Threshold
    # ============================

    MIN_CONFIDENCE: float = 0.75


@lru_cache
def get_settings():

    return Settings()


settings = get_settings()