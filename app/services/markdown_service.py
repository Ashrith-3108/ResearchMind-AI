from pathlib import Path

from app.services.logger_service import logger


class MarkdownService:
    """
    Markdown Service

    Responsibilities
    ----------------
    • Save Markdown reports
    • Load Markdown reports
    • Ensure directories exist
    """

    def save(
        self,
        markdown: str,
        output_path,
    ) -> str:

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            output_path,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(markdown)

        logger.info(
            f"Markdown saved -> {output_path}"
        )

        return str(output_path)

    def load(
        self,
        file_path,
    ) -> str:

        file_path = Path(file_path)

        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as file:

            return file.read()

    def append(
        self,
        text: str,
        file_path,
    ):

        file_path = Path(file_path)

        with open(
            file_path,
            "a",
            encoding="utf-8",
        ) as file:

            file.write(text)

        logger.info(
            f"Markdown updated -> {file_path}"
        )


markdown_service = MarkdownService()