from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
)

from app.services.logger_service import logger


class PDFReportService:
    """
    PDF Report Service

    Responsibilities
    ----------------
    • Convert Markdown to PDF
    • Save PDF reports
    • Return generated PDF path
    """

    def generate(
        self,
        markdown_text: str,
        output_path,
    ) -> str:

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        styles = getSampleStyleSheet()

        doc = SimpleDocTemplate(str(output_path))

        story = []

        for line in markdown_text.split("\n"):

            line = line.strip()

            if not line:
                continue

            # -----------------------------
            # Markdown Headings
            # -----------------------------

            if line.startswith("# "):
                story.append(
                    Paragraph(
                        f"<font size=22><b>{line[2:]}</b></font>",
                        styles["Title"],
                    )
                )

            elif line.startswith("## "):
                story.append(
                    Paragraph(
                        f"<font size=18><b>{line[3:]}</b></font>",
                        styles["Heading1"],
                    )
                )

            elif line.startswith("### "):
                story.append(
                    Paragraph(
                        f"<font size=15><b>{line[4:]}</b></font>",
                        styles["Heading2"],
                    )
                )

            # -----------------------------
            # Bullet Points
            # -----------------------------

            elif line.startswith("- "):

                story.append(
                    Paragraph(
                        f"• {line[2:]}",
                        styles["BodyText"],
                    )
                )

            # -----------------------------
            # Horizontal Rule
            # -----------------------------

            elif line.startswith("---"):

                story.append(
                    Paragraph(
                        "<br/>",
                        styles["BodyText"],
                    )
                )

            # -----------------------------
            # Normal Paragraph
            # -----------------------------

            else:

                story.append(
                    Paragraph(
                        line,
                        styles["BodyText"],
                    )
                )

        doc.build(story)

        logger.info(
            f"PDF report saved -> {output_path}"
        )

        return str(output_path)


pdf_report_service = PDFReportService()