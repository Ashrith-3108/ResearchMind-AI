from app.models.state import ResearchState


def create_initial_state(
    paper_text: str,
    pdf_path: str = "",
) -> ResearchState:
    """
    Creates the initial workflow state.

    This is the single entry point for the LangGraph workflow.
    """

    return ResearchState(
        pdf_path=pdf_path,
        paper_text=paper_text,

        current_agent="metadata",

        execution_plan=[
            "metadata",
            "analyzer",
            "reviewer",
            "summarizer",
            "citation",
            "insights",
            "fact_checker",
            "hallucination",
            "confidence",
            "report_generator",
            "exporter",
        ],

        completed_agents=[],

        retry_count=0,

        max_retries=2,

        review_score=0.0,

        approved=False,

        metadata={},

        analysis={},

        summary={},

        citations={},

        insights={},

        review={},

        fact_check={},

        hallucination={},

        confidence={},

        final_report={},

        exported_files={},

        status="initialized",

        error=None,
    )