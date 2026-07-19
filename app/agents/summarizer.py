from app.agents.base_agent import BaseAgent
from app.models.outputs import SummaryOutput
from app.prompts import SUMMARY_PROMPT
from app.services.logger_service import logger


class SummarizerAgent(BaseAgent):
    """
    Summarizer Agent

    Responsibilities
    ----------------
    • Generate three summaries
        - Executive Summary
        - Technical Summary
        - Beginner Summary

    Rules
    -----
    • Use ONLY the provided analysis.
    • Never invent facts.
    • Never introduce new datasets, metrics,
      experiments, or references.
    • If information is unavailable,
      state "Not specified in the paper."
    """

    def run(self, analysis: dict):

        logger.info("Running Summarizer Agent...")

        prompt = f"""
{SUMMARY_PROMPT}

STRICT RULES

You are NOT allowed to add any new information.

Only summarize the information provided below.

DO NOT:

- invent datasets
- invent experiments
- invent results
- invent performance metrics
- invent references
- invent future work
- invent applications
- invent implementation details

If any field contains:

"Not specified in the paper."

keep it unchanged.

If results are:

"Not reported."

do not replace them.

Return ONLY valid JSON.

Schema

{{
    "executive_summary": "",
    "technical_summary": "",
    "beginner_summary": ""
}}

Research Analysis

{analysis}
"""

        result = super().run(
            prompt,
            SummaryOutput,
        )

        logger.info("Summarizer completed successfully.")

        return result


summarizer = SummarizerAgent()