from typing import Dict, List, Optional

from pydantic import BaseModel, Field


# ==========================================================
# Upload Response
# ==========================================================

class UploadResponse(BaseModel):

    success: bool

    filename: str

    message: str


# ==========================================================
# Analyze Request
# ==========================================================

class AnalyzeRequest(BaseModel):

    pdf_path: str


# ==========================================================
# Exported Files
# ==========================================================

class ExportedFiles(BaseModel):

    markdown: Optional[str] = None

    json: Optional[str] = None

    pdf: Optional[str] = None


# ==========================================================
# Metadata
# ==========================================================

class MetadataSchema(BaseModel):

    title: str = "Not specified in the paper."

    authors: List[str] = Field(default_factory=list)

    abstract: str = "Not specified in the paper."

    keywords: List[str] = Field(default_factory=list)

    institution: str = "Not specified in the paper."

    department: str = "Not specified in the paper."

    year: str = "Not specified in the paper."

    venue: str = "Not specified in the paper."

    domain: str = "Not specified in the paper."

    doi: str = "Not specified in the paper."

    emails: List[str] = Field(default_factory=list)


# ==========================================================
# Analyze Response
# ==========================================================

class AnalyzeResponse(BaseModel):

    success: bool

    metadata: Dict = Field(default_factory=dict)

    analysis: Dict = Field(default_factory=dict)

    summary: Dict = Field(default_factory=dict)

    citations: Dict = Field(default_factory=dict)

    insights: Dict = Field(default_factory=dict)

    review: Dict = Field(default_factory=dict)

    fact_check: Dict = Field(default_factory=dict)

    hallucination: Dict = Field(default_factory=dict)

    confidence: Dict = Field(default_factory=dict)

    final_report: Dict = Field(default_factory=dict)

    exported_files: ExportedFiles


# ==========================================================
# Health Response
# ==========================================================

class HealthResponse(BaseModel):

    status: str

    service: str


# ==========================================================
# Version Response
# ==========================================================

class VersionResponse(BaseModel):

    application: str

    version: str


# ==========================================================
# Error Response
# ==========================================================

class ErrorResponse(BaseModel):

    success: bool = False

    error: str

    detail: Optional[str] = None