from app.agents.base_agent import BaseAgent
from app.models.outputs import CitationOutput
from app.prompts import CITATION_PROMPT
from app.services.logger_service import logger


class CitationAgent(BaseAgent):
    """
    Citation Agent

    Responsibilities
    ----------------
    • Extract citations explicitly mentioned.
    • Extract references explicitly listed.
    • Extract related work only if present.
    """

    def run(self, analysis: dict):

        logger.info("Running Citation Agent...")

        prompt = f"""
{CITATION_PROMPT}

STRICT INSTRUCTIONS

Extract ONLY information explicitly present in the research paper.

DO NOT:

- invent citations
- invent references
- invent authors
- invent paper titles
- invent journals
- invent conferences
- invent publication years
- invent DOIs
- invent related work
- use outside knowledge
- search the internet

Rules

If no citations exist:

Return:

[]

If no references exist:

Return:

[]

If no related work exists:

Return:

[]

Return ONLY valid JSON.

Schema

{{
    "citations": [],
    "references": [],
    "related_work": []
}}

Research Analysis

{analysis}
"""

        result = super().run(
            prompt,
            CitationOutput,
        )

        logger.info("Citation extraction completed.")

        return result


citation = CitationAgent()