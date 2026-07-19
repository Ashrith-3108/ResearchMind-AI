from app.agents.base_agent import BaseAgent
from app.models.outputs import FactCheckOutput
from app.prompts import FACTCHECK_PROMPT
from app.services.logger_service import logger


class FactCheckerAgent(BaseAgent):
    """
    Fact Checker Agent

    Responsibilities
    ----------------
    • Verify that every generated statement
      is supported by the research paper.

    • Detect unsupported claims.

    • Detect hallucinated facts.

    • Never use outside knowledge.

    • Never search the internet.
    """

    def run(
        self,
        paper: str,
        analysis: dict,
        summary: dict,
    ):

        logger.info("Running Fact Checker Agent...")

        prompt = f"""
{FACTCHECK_PROMPT}

STRICT INSTRUCTIONS

You are NOT allowed to use outside knowledge.

You are NOT allowed to search the internet.

Compare the generated outputs ONLY with the
original research paper.

For every important statement decide whether it is

- Supported
- Unsupported
- Unverifiable

DO NOT invent evidence.

DO NOT fabricate missing facts.

If every statement is supported:

hallucinations = []

unsupported_claims = []

overall_status = "Verified"

If unsupported claims exist,
list them exactly.

Return ONLY valid JSON.

Schema

{{
    "supported_claims": [],
    "unsupported_claims": [],
    "hallucinations": [],
    "overall_status": ""
}}

Original Research Paper

{paper}

Analysis

{analysis}

Summary

{summary}
"""

        result = super().run(
            prompt,
            FactCheckOutput,
        )

        logger.info("Fact Checker completed.")

        return result


fact_checker = FactCheckerAgent()