from datetime import datetime
from pathlib import Path

from app.services.json_service import json_service
from app.services.markdown_service import markdown_service
from app.services.pdf_report_service import pdf_report_service
from app.services.logger_service import logger


class ExporterAgent:
    """
    Exporter Agent

    Responsibilities
    ----------------
    • Save Markdown report
    • Save JSON report
    • Save PDF report
    • Return exported file paths
    """

    def __init__(self):

        self.markdown_dir = Path("outputs/markdown")
        self.json_dir = Path("outputs/json")
        self.pdf_dir = Path("outputs/pdf")

        self.markdown_dir.mkdir(parents=True, exist_ok=True)
        self.json_dir.mkdir(parents=True, exist_ok=True)
        self.pdf_dir.mkdir(parents=True, exist_ok=True)

    def run(
        self,
        final_report: dict,
    ):

        logger.info("Exporting reports...")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        markdown_file = (
            self.markdown_dir
            / f"research_report_{timestamp}.md"
        )

        json_file = (
            self.json_dir
            / f"research_report_{timestamp}.json"
        )

        pdf_file = (
            self.pdf_dir
            / f"research_report_{timestamp}.pdf"
        )

        # -------------------------------------------------
        # Markdown
        # -------------------------------------------------

        markdown_service.save(
            final_report["markdown"],
            markdown_file,
        )

        # -------------------------------------------------
        # JSON
        # -------------------------------------------------

        json_service.save(
            final_report["report_json"],
            json_file,
        )

        # -------------------------------------------------
        # PDF
        # -------------------------------------------------

        pdf_report_service.generate(
            markdown_text=final_report["markdown"],
            output_path=pdf_file,
        )

        logger.info("Export completed successfully.")

        return {
            "markdown": str(markdown_file),
            "json": str(json_file),
            "pdf": str(pdf_file),
        }


exporter = ExporterAgent()