from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.graph.state import create_initial_state
from app.graph.workflow import run_workflow
from app.services.pdf_service import pdf_service
from app.services.logger_service import logger

router = APIRouter(
    prefix="/api",
    tags=["ResearchMind AI"],
)


# ==========================================================
# Analyze Research Paper
# ==========================================================

@router.post("/analyze")
async def analyze_paper(
    file: UploadFile = File(...),
):
    """
    Upload a research paper and analyze it.
    """

    if not file.filename.lower().endswith(".pdf"):

        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported.",
        )

    try:

        logger.info(
            f"Received file: {file.filename}"
        )

        upload_dir = Path("sample_input")

        upload_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        pdf_path = upload_dir / file.filename

        with open(pdf_path, "wb") as f:

            f.write(await file.read())

        paper = pdf_service.extract_text(
            str(pdf_path)
        )

        state = create_initial_state(
            paper_text=paper,
            pdf_path=str(pdf_path),
        )

        result = run_workflow(state)

        logger.info("Analysis completed.")

        return {
            "success": True,
            "report": result.final_report,
            "exported_files": result.exported_files,
        }

    except Exception as e:

        logger.exception(e)

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# ==========================================================
# Health
# ==========================================================

@router.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "ResearchMind AI",
    }


# ==========================================================
# Version
# ==========================================================

@router.get("/version")
def version():

    return {
        "application": "ResearchMind AI",
        "version": "1.0.0",
    }


# ==========================================================
# Exported Reports
# ==========================================================

@router.get("/reports")
def reports():

    reports = Path("outputs")

    markdown = list(
        (reports / "markdown").glob("*.md")
    )

    json_files = list(
        (reports / "json").glob("*.json")
    )

    pdfs = list(
        (reports / "pdf").glob("*.pdf")
    )

    return {
        "markdown": [str(i) for i in markdown],
        "json": [str(i) for i in json_files],
        "pdf": [str(i) for i in pdfs],
    }