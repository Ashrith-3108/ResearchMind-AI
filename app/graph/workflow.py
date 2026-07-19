from langgraph.graph import StateGraph, END

from app.models.state import ResearchState

from app.services.logger_service import logger

from app.agents.metadata import metadata
from app.agents.analyzer import analyzer
from app.agents.summarizer import summarizer
from app.agents.citation import citation
from app.agents.insights import insight
from app.agents.reviewer import reviewer
from app.agents.fact_checker import fact_checker
from app.agents.hallucination import hallucination
from app.agents.confidence import confidence
from app.agents.report_generator import report_generator
from app.agents.exporter import exporter

from app.graph.conditional import (
    route_after_metadata,
    route_after_analyzer,
    route_after_review,
    route_after_summary,
    route_after_citation,
    route_after_insight,
    route_after_fact_checker,
    route_after_hallucination,
    route_after_confidence,
    route_after_report,
    route_after_export,
)

# ==========================================================
# METADATA NODE
# ==========================================================

def metadata_node(state: ResearchState):

    logger.info("Running Metadata Agent")

    result = metadata.run(state.paper_text)

    state.metadata = result.model_dump()

    state.completed_agents.append("metadata")

    return state


# ==========================================================
# ANALYZER NODE
# ==========================================================

def analyzer_node(state: ResearchState):

    logger.info("Running Analyzer Agent")

    result = analyzer.run(state.paper_text)

    state.analysis = result.model_dump()

    state.completed_agents.append("analyzer")

    return state


# ==========================================================
# REVIEWER NODE
# ==========================================================

def reviewer_node(state: ResearchState):

    logger.info("Running Reviewer Agent")

    result = reviewer.run(
        state.analysis,
        state.summary,
        state.insights,
    )

    state.review = result.model_dump()

    state.review_score = result.score

    state.approved = result.approved

    state.completed_agents.append("reviewer")

    return state


# ==========================================================
# SUMMARY NODE
# ==========================================================

def summary_node(state: ResearchState):

    logger.info("Running Summarizer Agent")

    result = summarizer.run(state.analysis)

    state.summary = result.model_dump()

    state.completed_agents.append("summarizer")

    return state


# ==========================================================
# CITATION NODE
# ==========================================================

def citation_node(state: ResearchState):

    logger.info("Running Citation Agent")

    result = citation.run(state.analysis)

    state.citations = result.model_dump()

    state.completed_agents.append("citation")

    return state
# ==========================================================
# INSIGHT NODE
# ==========================================================

def insight_node(state: ResearchState):

    logger.info("Running Insight Agent")

    result = insight.run(
        state.analysis,
    )

    state.insights = result.model_dump()

    state.completed_agents.append("insight")

    return state


# ==========================================================
# FACT CHECKER NODE
# ==========================================================

def fact_checker_node(state: ResearchState):

    logger.info("Running Fact Checker Agent")

    result = fact_checker.run(
        paper=state.paper_text,
        analysis=state.analysis,
        summary=state.summary,
    )

    state.fact_check = result.model_dump()

    state.completed_agents.append("fact_checker")

    return state


# ==========================================================
# HALLUCINATION NODE
# ==========================================================

def hallucination_node(state: ResearchState):

    logger.info("Running Hallucination Agent")

    result = hallucination.run(
        paper=state.paper_text,
        analysis=state.analysis,
        summary=state.summary,
        insights=state.insights,
    )

    state.hallucination = result.model_dump()

    state.completed_agents.append("hallucination")

    return state


# ==========================================================
# CONFIDENCE NODE
# ==========================================================

def confidence_node(state: ResearchState):

    logger.info("Running Confidence Agent")

    result = confidence.run(
        analysis=state.analysis,
        summary=state.summary,
        citations=state.citations,
        insights=state.insights,
        review=state.review,
    )

    state.confidence = result.model_dump()

    state.completed_agents.append("confidence")

    return state


# ==========================================================
# REPORT NODE
# ==========================================================

def report_node(state: ResearchState):

    logger.info("Running Report Generator")

    report = report_generator.run(
        metadata=state.metadata,
        analysis=state.analysis,
        summary=state.summary,
        citations=state.citations,
        insights=state.insights,
        review=state.review,
        fact_check=state.fact_check,
        hallucination=state.hallucination,
        confidence=state.confidence,
    )

    state.final_report = report

    state.completed_agents.append("report_generator")

    return state


# ==========================================================
# EXPORTER NODE
# ==========================================================

def exporter_node(state: ResearchState):

    logger.info("Running Exporter Agent")

    exported = exporter.run(
        state.final_report,
    )

    state.exported_files = exported

    state.completed_agents.append("exporter")

    return state
# ==========================================================
# BUILD LANGGRAPH
# ==========================================================

builder = StateGraph(ResearchState)


# ==========================================================
# REGISTER NODES
# ==========================================================

builder.add_node("metadata", metadata_node)

builder.add_node("analyzer", analyzer_node)

builder.add_node("review", reviewer_node)

builder.add_node("summary", summary_node)

builder.add_node("citation", citation_node)

builder.add_node("insight", insight_node)

builder.add_node("fact_checker", fact_checker_node)

builder.add_node("hallucination", hallucination_node)

builder.add_node("confidence", confidence_node)

builder.add_node("report", report_node)

builder.add_node("export", exporter_node)


# ==========================================================
# ENTRY POINT
# ==========================================================

builder.set_entry_point("metadata")


# ==========================================================
# CONDITIONAL EDGES
# ==========================================================

builder.add_conditional_edges(
    "metadata",
    route_after_metadata,
    {
        "analyzer": "analyzer",
    },
)

builder.add_conditional_edges(
    "analyzer",
    route_after_analyzer,
    {
        "review": "review",
    },
)

builder.add_conditional_edges(
    "review",
    route_after_review,
    {
        "analyzer": "analyzer",
        "summary": "summary",
    },
)

builder.add_conditional_edges(
    "summary",
    route_after_summary,
    {
        "citation": "citation",
    },
)

builder.add_conditional_edges(
    "citation",
    route_after_citation,
    {
        "insight": "insight",
    },
)

builder.add_conditional_edges(
    "insight",
    route_after_insight,
    {
        "fact_checker": "fact_checker",
    },
)

builder.add_conditional_edges(
    "fact_checker",
    route_after_fact_checker,
    {
        "hallucination": "hallucination",
    },
)

builder.add_conditional_edges(
    "hallucination",
    route_after_hallucination,
    {
        "confidence": "confidence",
    },
)

builder.add_conditional_edges(
    "confidence",
    route_after_confidence,
    {
        "report": "report",
    },
)

builder.add_conditional_edges(
    "report",
    route_after_report,
    {
        "export": "export",
    },
)

builder.add_conditional_edges(
    "export",
    route_after_export,
    {
        "__end__": END,
    },
)
# ==========================================================
# COMPILE GRAPH
# ==========================================================

graph = builder.compile()


# ==========================================================
# RUN WORKFLOW
# ==========================================================

def run_workflow(
    state: ResearchState,
) -> ResearchState:
    """
    Execute the complete LangGraph workflow.

    Parameters
    ----------
    state : ResearchState

    Returns
    -------
    ResearchState
    """

    logger.info("=" * 80)
    logger.info("Starting ResearchMind AI Workflow")
    logger.info("=" * 80)

    result = graph.invoke(state)

    # graph.invoke() returns a dict in newer LangGraph versions
    if isinstance(result, dict):
        result = ResearchState(**result)

    logger.info("=" * 80)
    logger.info("Workflow Completed Successfully")
    logger.info("=" * 80)

    return result


# ==========================================================
# STREAM WORKFLOW
# ==========================================================

def stream_workflow(
    state: ResearchState,
):
    """
    Stream workflow execution.

    Useful for:
    • Streamlit
    • FastAPI
    • WebSockets
    """

    logger.info("Streaming workflow...")

    for event in graph.stream(state):
        yield event


# ==========================================================
# GRAPH ACCESSOR
# ==========================================================

def get_graph():
    """
    Returns the compiled graph.
    """

    return graph


# ==========================================================
# DEBUG
# ==========================================================

if __name__ == "__main__":

    print(graph)