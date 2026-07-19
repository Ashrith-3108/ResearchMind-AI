from typing import List, Optional

from pydantic import BaseModel, Field


class ResearchState(BaseModel):
    """
    Shared state used across the entire LangGraph workflow.
    """

    # ==========================================================
    # INPUT
    # ==========================================================

    pdf_path: Optional[str] = None
    paper_text: Optional[str] = None

    # ==========================================================
    # WORKFLOW
    # ==========================================================

    current_agent: str = "boss"

    execution_plan: List[str] = Field(default_factory=list)

    completed_agents: List[str] = Field(default_factory=list)

    # ==========================================================
    # RETRY MANAGEMENT
    # ==========================================================

    retry_count: int = 0

    max_retries: int = 2

    review_score: float = 0.0

    approved: bool = False

    # ==========================================================
    # METADATA
    # ==========================================================

    metadata: dict = Field(default_factory=dict)

    # ==========================================================
    # AGENT OUTPUTS
    # ==========================================================

    analysis: dict = Field(default_factory=dict)

    summary: dict = Field(default_factory=dict)

    citations: dict = Field(default_factory=dict)

    insights: dict = Field(default_factory=dict)

    review: dict = Field(default_factory=dict)

    fact_check: dict = Field(default_factory=dict)

    hallucination: dict = Field(default_factory=dict)

    confidence: dict = Field(default_factory=dict)

    # ==========================================================
    # FINAL REPORT
    # ==========================================================

    final_report: dict = Field(default_factory=dict)

    exported_files: dict = Field(default_factory=dict)

    # ==========================================================
    # EXECUTION INFO
    # ==========================================================

    status: str = "initialized"

    error: Optional[str] = None