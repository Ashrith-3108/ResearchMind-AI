from app.agents.base_agent import BaseAgent
from app.models.outputs import InsightOutput
from app.prompts import INSIGHT_PROMPT
from app.services.logger_service import logger


class InsightAgent(BaseAgent):
    """
    Insight Agent

    Responsibilities
    ----------------
    • Extract key insights from the research.
    • Identify future work if explicitly mentioned.
    • Identify practical applications if explicitly mentioned.
    • Never hallucinate information.
    """

    def run(self, analysis: dict):

        logger.info("Running Insight Agent...")

        prompt = f"""
{INSIGHT_PROMPT}

STRICT INSTRUCTIONS

Generate insights ONLY from the supplied analysis.

DO NOT:

- invent datasets
- invent experiments
- invent results
- invent references
- invent future work
- invent applications
- invent implementation details
- invent performance metrics
- use outside knowledge
- search the internet

Rules

Key Insights

• Only include insights directly supported by the analysis.

• If there are no meaningful insights:

Return

[]

Future Work

• Return future work ONLY if it is explicitly mentioned.

Otherwise return exactly

"Not specified in the paper."

Applications

• Return applications ONLY if explicitly mentioned.

Otherwise return

[]

Return ONLY valid JSON.

Schema

{{
    "key_insights": [],
    "future_work": "",
    "applications": []
}}

Research Analysis

{analysis}
"""

        result = super().run(
            prompt,
            InsightOutput,
        )

        logger.info("Insight extraction completed.")

        return result


insight = InsightAgent()