from typing import List

from pydantic import BaseModel, Field


# =====================================================
# Metadata
# =====================================================

class MetadataOutput(BaseModel):

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


# =====================================================
# Analyzer
# =====================================================

class AnalysisOutput(BaseModel):

    problem_statement: str

    methodology: str

    experiments: str

    datasets: List[str]

    results: str

    limitations: str


# =====================================================
# Summary
# =====================================================

class SummaryOutput(BaseModel):

    executive_summary: str

    technical_summary: str

    beginner_summary: str


# =====================================================
# Citation
# =====================================================

class CitationOutput(BaseModel):

    citations: List[str]

    references: List[str]

    related_work: List[str]


# =====================================================
# Insights
# =====================================================

class InsightOutput(BaseModel):

    key_insights: List[str] = Field(default_factory=list)

    future_work: str = "Not specified in the paper."

    applications: List[str] = Field(default_factory=list)


# =====================================================
# Review
# =====================================================

class ReviewOutput(BaseModel):

    score: float

    feedback: str

    approved: bool


# =====================================================
# Fact Checker
# =====================================================

class FactCheckOutput(BaseModel):

    supported_claims: List[str]

    unsupported_claims: List[str]

    hallucinations: List[str]

    overall_status: str


# =====================================================
# Hallucination
# =====================================================

class HallucinationOutput(BaseModel):

    hallucination_detected: bool

    hallucinations: List[str]

    severity: str

    recommendation: str


# =====================================================
# Confidence
# =====================================================

class ConfidenceOutput(BaseModel):

    overall_confidence: float

    analysis_confidence: float

    summary_confidence: float

    citation_confidence: float

    insight_confidence: float

    review_confidence: float

    weak_sections: List[str]

    recommendation: str