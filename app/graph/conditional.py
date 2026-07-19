from app.services.logger_service import logger
from app.models.state import ResearchState


def route_after_metadata(state: ResearchState):

    logger.info("Metadata completed.")

    state.current_agent = "analyzer"

    return "analyzer"


def route_after_analyzer(state: ResearchState):

    logger.info("Analysis completed.")

    state.current_agent = "review"

    return "review"


def route_after_review(state: ResearchState):

    logger.info("Review completed.")

    score = state.review_score

    # If the review score is low, log it but continue.
    if score < 7:
        logger.warning(
            f"Review score is {score}. Continuing workflow."
        )

    state.current_agent = "summary"

    return "summary"


def route_after_summary(state: ResearchState):

    logger.info("Summary completed.")

    state.current_agent = "citation"

    return "citation"


def route_after_citation(state: ResearchState):

    logger.info("Citation extraction completed.")

    state.current_agent = "insight"

    return "insight"


def route_after_insight(state: ResearchState):

    logger.info("Insight generation completed.")

    state.current_agent = "fact_checker"

    return "fact_checker"


def route_after_fact_checker(state: ResearchState):

    logger.info("Fact checking completed.")

    state.current_agent = "hallucination"

    return "hallucination"


def route_after_hallucination(state: ResearchState):

    logger.info("Hallucination detection completed.")

    state.current_agent = "confidence"

    return "confidence"


def route_after_confidence(state: ResearchState):

    logger.info("Confidence scoring completed.")

    state.current_agent = "report"

    return "report"


def route_after_report(state: ResearchState):

    logger.info("Report generated.")

    state.current_agent = "export"

    return "export"


def route_after_export(state: ResearchState):

    logger.info("Workflow completed.")

    state.current_agent = "completed"

    state.status = "completed"

    return "__end__"