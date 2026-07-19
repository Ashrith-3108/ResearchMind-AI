from pathlib import Path
import time

from app.graph.state import create_initial_state
from app.graph.workflow import run_workflow

from app.services.pdf_service import pdf_service
from app.services.logger_service import logger

from app.utils.validators import validator


# ==========================================================
# CONFIG
# ==========================================================

PDF_PATH = "sample_input/paper.pdf"


# ==========================================================
# MAIN
# ==========================================================

def main():

    start = time.time()

    logger.info("=" * 80)
    logger.info("ResearchMind AI Started")
    logger.info("=" * 80)

    try:

        # ----------------------------------------------------
        # Validate PDF
        # ----------------------------------------------------

        validator.validate_pdf(PDF_PATH)

        validator.validate_file_size(PDF_PATH)

        # ----------------------------------------------------
        # Extract Text
        # ----------------------------------------------------

        logger.info("Extracting PDF...")

        paper = pdf_service.extract_text(PDF_PATH)

        validator.validate_text(paper)

        # ----------------------------------------------------
        # Create Workflow State
        # ----------------------------------------------------

        state = create_initial_state(
            paper_text=paper,
            pdf_path=PDF_PATH,
        )

        # ----------------------------------------------------
        # Run Workflow
        # ----------------------------------------------------

        result = run_workflow(state)

        logger.info("Workflow Finished")

        # ----------------------------------------------------
        # Display Results
        # ----------------------------------------------------

        print("\n")
        print("=" * 80)
        print("FINAL REPORT")
        print("=" * 80)
        print()

        print(result.final_report["markdown"])

        print()

        print("=" * 80)
        print("EXPORTED FILES")
        print("=" * 80)

        for k, v in result.exported_files.items():

            print(f"{k.upper():10} : {v}")

        print()

        print("=" * 80)
        print("QUALITY")
        print("=" * 80)

        print(
            f"Review Score : {result.review.get('score')}"
        )

        print(
            f"Approved    : {result.review.get('approved')}"
        )

        print(
            f"Confidence  : {result.confidence.get('overall_confidence')}"
        )

        end = time.time()

        print()
        print("=" * 80)
        print(
            f"Completed in {round(end-start,2)} seconds"
        )
        print("=" * 80)

        logger.info("ResearchMind AI Finished Successfully")

    except Exception as e:

        logger.exception(e)

        print("\nERROR\n")

        print(str(e))


# ==========================================================
# ENTRY
# ==========================================================

if __name__ == "__main__":

    main()