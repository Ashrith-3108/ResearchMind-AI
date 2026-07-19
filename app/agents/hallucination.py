from app.agents.base_agent import BaseAgent
from app.models.outputs import HallucinationOutput
from app.prompts import HALLUCINATION_PROMPT
from app.services.logger_service import logger


class HallucinationAgent(BaseAgent):
    """
    Hallucination Detection Agent

    Responsibilities
    ----------------
    • Detect fabricated information.
    • Detect unsupported claims.
    • Detect invented datasets.
    • Detect invented experiments.
    • Detect invented references.
    • Detect invented metrics.
    • Detect invented implementation details.
    """

    def run(
        self,
        paper: str,
        analysis: dict,
        summary: dict,
        insights: dict,
    ):

        logger.info("Running Hallucination Agent...")

        prompt = f"""
{HALLUCINATION_PROMPT}

STRICT INSTRUCTIONS

Your ONLY job is to compare the generated outputs
against the original paper.

DO NOT use outside knowledge.

DO NOT search the internet.

A hallucination means information that
does NOT exist in the original paper.

Check for:

- invented datasets
- invented experiments
- invented references
- invented citations
- invented metrics
- invented accuracy
- invented precision
- invented recall
- invented F1-score
- invented ROC
- invented AUC
- invented implementation details
- invented future work
- invented applications
- invented conclusions

If none exist

Return

hallucination_detected = false

hallucinations = []

Otherwise

hallucination_detected = true

and list every hallucinated statement.

Return ONLY valid JSON.

Schema

{{
    "hallucination_detected": false,
    "hallucinations": [],
    "severity": "Low",
    "recommendation": ""
}}

Original Paper

{paper}

Analysis

{analysis}

Summary

{summary}

Insights

{insights}
"""

        result = super().run(
            prompt,
            HallucinationOutput,
        )

        logger.info("Hallucination detection completed.")

        return result


hallucination = HallucinationAgent()