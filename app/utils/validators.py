import json
from pathlib import Path
from typing import Any

from app.config import settings


class Validator:
    """
    Validation utilities used across ResearchMind AI.
    """

    # =====================================================
    # FILE VALIDATION
    # =====================================================

    def validate_pdf(self, pdf_path: str):

        path = Path(pdf_path)

        if not path.exists():
            raise FileNotFoundError(
                f"PDF not found: {pdf_path}"
            )

        if path.suffix.lower() != ".pdf":
            raise ValueError(
                "Only PDF files are supported."
            )

        return True

    # =====================================================
    # FILE SIZE
    # =====================================================

    def validate_file_size(self, pdf_path: str):

        path = Path(pdf_path)

        size_mb = path.stat().st_size / (1024 * 1024)

        if size_mb > settings.MAX_FILE_SIZE_MB:

            raise ValueError(
                f"Maximum file size is "
                f"{settings.MAX_FILE_SIZE_MB} MB."
            )

        return True

    # =====================================================
    # TEXT
    # =====================================================

    def validate_text(self, text: str):

        if text is None:

            raise ValueError(
                "Text cannot be None."
            )

        if len(text.strip()) == 0:

            raise ValueError(
                "Text is empty."
            )

        return True

    # =====================================================
    # JSON
    # =====================================================

    def validate_json(self, data: Any):

        try:

            if isinstance(data, str):

                json.loads(data)

            else:

                json.dumps(data)

            return True

        except Exception:

            return False

    # =====================================================
    # LLM RESPONSE
    # =====================================================

    def validate_llm_response(
        self,
        response,
    ):

        if response is None:

            raise ValueError(
                "LLM returned None."
            )

        if not hasattr(response, "content"):

            raise ValueError(
                "Invalid LLM response."
            )

        if not response.content:

            raise ValueError(
                "Empty LLM response."
            )

        return True

    # =====================================================
    # REQUIRED KEYS
    # =====================================================

    def validate_keys(
        self,
        data: dict,
        required_keys: list,
    ):

        missing = []

        for key in required_keys:

            if key not in data:

                missing.append(key)

        if missing:

            raise ValueError(
                f"Missing keys: {missing}"
            )

        return True

    # =====================================================
    # REPORT
    # =====================================================

    def validate_report(
        self,
        report: dict,
    ):

        required = [
            "markdown",
            "report_json",
        ]

        self.validate_keys(
            report,
            required,
        )

        return True

    # =====================================================
    # CONFIDENCE
    # =====================================================

    def validate_confidence(
        self,
        score: float,
    ):

        if score < 0 or score > 100:

            raise ValueError(
                "Confidence score must be between 0 and 100."
            )

        return True

    # =====================================================
    # REVIEW SCORE
    # =====================================================

    def validate_review_score(
        self,
        score: float,
    ):

        if score < 0 or score > 10:

            raise ValueError(
                "Review score must be between 0 and 10."
            )

        return True

    # =====================================================
    # OUTPUT DIRECTORY
    # =====================================================

    def validate_directory(
        self,
        directory: str,
    ):

        Path(directory).mkdir(
            parents=True,
            exist_ok=True,
        )

        return True


validator = Validator()