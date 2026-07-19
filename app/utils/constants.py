"""
ResearchMind AI Constants
"""

from pathlib import Path


# ==========================================================
# APPLICATION
# ==========================================================

APP_NAME = "ResearchMind AI"

APP_VERSION = "1.0.0"

COMPANY = "ResearchMind"


# ==========================================================
# DIRECTORIES
# ==========================================================

BASE_DIR = Path(".")

APP_DIR = BASE_DIR / "app"

OUTPUT_DIR = BASE_DIR / "outputs"

MARKDOWN_DIR = OUTPUT_DIR / "markdown"

JSON_DIR = OUTPUT_DIR / "json"

PDF_DIR = OUTPUT_DIR / "pdf"

REPORT_DIR = OUTPUT_DIR / "reports"

INPUT_DIR = BASE_DIR / "sample_input"

LOG_DIR = BASE_DIR / "storage" / "logs"

CACHE_DIR = BASE_DIR / "storage" / "cache"

EMBEDDING_DIR = BASE_DIR / "storage" / "embeddings"


# ==========================================================
# FILES
# ==========================================================

DEFAULT_REPORT_NAME = "research_report"

DEFAULT_LOG_FILE = LOG_DIR / "researchmind.log"


# ==========================================================
# LLM
# ==========================================================

DEFAULT_TEMPERATURE = 0

DEFAULT_TOP_P = 1

DEFAULT_TIMEOUT = 120


# ==========================================================
# PDF
# ==========================================================

SUPPORTED_FILE_TYPES = [
    ".pdf",
]

MAX_FILE_SIZE_MB = 50


# ==========================================================
# CHUNKING
# ==========================================================

DEFAULT_CHUNK_SIZE = 1200

DEFAULT_CHUNK_OVERLAP = 200


# ==========================================================
# REVIEW
# ==========================================================

PASS_SCORE = 7.0

MAX_RETRIES = 2


# ==========================================================
# CONFIDENCE
# ==========================================================

HIGH_CONFIDENCE = 85

MEDIUM_CONFIDENCE = 70

LOW_CONFIDENCE = 50


# ==========================================================
# EXPORTS
# ==========================================================

EXPORT_MARKDOWN = True

EXPORT_JSON = True

EXPORT_PDF = True


# ==========================================================
# WORKFLOW
# ==========================================================

WORKFLOW = [
    "metadata",
    "analyzer",
    "reviewer",
    "summarizer",
    "citation",
    "insights",
    "fact_checker",
    "hallucination",
    "confidence",
    "report_generator",
    "exporter",
]


# ==========================================================
# STATUS
# ==========================================================

STATUS_INITIALIZED = "initialized"

STATUS_RUNNING = "running"

STATUS_COMPLETED = "completed"

STATUS_FAILED = "failed"