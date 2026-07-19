import json

from app.services.llm_service import llm_service
from app.services.logger_service import logger


class RouterAgent:
    """
    Router Agent

    Responsible for deciding which agent
    should execute next based on the
    current workflow state.

    This makes the workflow dynamic instead
    of hardcoded.
    """

    AVAILABLE_AGENTS = [
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
        "finish",
    ]

    def run(
        self,
        current_agent: str,
        completed_agents: list,
        execution_plan: list,
    ) -> str:

        logger.info("Routing workflow...")

        prompt = f"""
You are the Router Agent of ResearchMind AI.

Your job is to determine the NEXT agent.

Current Agent:
{current_agent}

Completed Agents:
{completed_agents}

Execution Plan:
{execution_plan}

Available Agents:
{self.AVAILABLE_AGENTS}

Rules:

- Follow the execution plan.
- Skip completed agents.
- Return ONLY JSON.
- If everything is completed return:

{{
    "next_agent":"finish"
}}

Otherwise return

{{
    "next_agent":"agent_name"
}}
"""

        response = llm_service.invoke(prompt)

        try:

            data = json.loads(response.content)

            next_agent = data["next_agent"]

            if next_agent not in self.AVAILABLE_AGENTS:

                logger.warning(
                    f"Invalid next agent: {next_agent}"
                )

                return "finish"

            logger.info(
                f"Next Agent -> {next_agent}"
            )

            return next_agent

        except Exception as e:

            logger.exception(e)

            return "finish"


router = RouterAgent()