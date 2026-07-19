import re
import fitz  # PyMuPDF


class PDFService:

    def extract_text(self, pdf_path: str) -> str:
        """
        Extract text from all pages of a PDF.
        """

        document = fitz.open(pdf_path)

        pages = []

        for page in document:
            text = page.get_text("text")

            if text:
                pages.append(text)

        document.close()

        full_text = "\n".join(pages)

        return self.clean_text(full_text)

    def clean_text(self, text: str) -> str:
        """
        Clean extracted text.
        """

        text = text.replace("\x00", "")

        # Join words split across lines
        text = re.sub(r"-\n", "", text)

        # Collapse multiple blank lines
        text = re.sub(r"\n{2,}", "\n", text)

        # Collapse multiple spaces
        text = re.sub(r"[ \t]+", " ", text)

        return text.strip()


pdf_service = PDFService()