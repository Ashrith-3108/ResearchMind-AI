from app.services.logger_service import logger
from app.services.pdf_service import pdf_service
from app.config import settings


class BossAgent:
    """
    Boss Agent

    The Boss Agent is the controller of the entire
    ResearchMind AI workflow.

    Responsibilities
    ----------------
    • Load research paper
    • Initialize workflow
    • Monitor workflow
    • Handle retries
    • Decide approval
    • Track execution
    """

    def load_paper(self, pdf_path: str):

        logger.info(f"Loading paper: {pdf_path}")

        paper_text = pdf_service.extract_text(pdf_path)

        logger.info("Paper loaded successfully.")

        return {
            "paper_text": paper_text,
            "status": "loaded",
            "retry_count": 0,
            "approved": False,
            "quality_score": 0.0,
            "current_agent": "metadata",
            "completed_agents": [],
            "execution_plan": [
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
        }

    def should_retry(
        self,
        score: float,
        retries: int,
    ) -> bool:

        if (
            score < 7.0
            and retries < settings.MAX_RETRIES
        ):
            logger.warning(
                f"Retry required. Score={score}, Retry={retries}"
            )
            return True

        return False

    def approve(
        self,
        score: float,
    ) -> bool:

        approved = score >= 7.0

        if approved:
            logger.info("Research paper approved.")
        else:
            logger.warning("Research paper rejected.")

        return approved

    def next_retry(
        self,
        state: dict,
    ):

        state["retry_count"] += 1

        logger.info(
            f"Retry Count : {state['retry_count']}"
        )

        return state

    def complete_agent(
        self,
        state: dict,
        agent_name: str,
    ):

        if agent_name not in state["completed_agents"]:
            state["completed_agents"].append(agent_name)

        state["current_agent"] = agent_name

        logger.info(
            f"{agent_name} completed."
        )

        return state

    def reset_workflow(
        self,
        state: dict,
    ):

        logger.info("Resetting workflow.")

        state["retry_count"] = 0
        state["approved"] = False
        state["quality_score"] = 0.0
        state["completed_agents"] = []
        state["current_agent"] = "metadata"

        return state


boss = BossAgent()