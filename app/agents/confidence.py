from app.agents.base_agent import BaseAgent
from app.models.outputs import ConfidenceOutput
from app.prompts import CONFIDENCE_PROMPT
from app.services.logger_service import logger


class ConfidenceAgent(BaseAgent):
    """
    Confidence Agent

    Responsibilities
    ----------------
    • Estimate confidence for every generated section.
    • Identify weak sections.
    • Recommend whether another analysis pass is needed.
    • Never invent information.
    """

    def run(
        self,
        analysis: dict,
        summary: dict,
        citations: dict,
        insights: dict,
        review: dict,
    ):

        logger.info("Running Confidence Agent...")

        prompt = f"""
{CONFIDENCE_PROMPT}

STRICT INSTRUCTIONS

Evaluate ONLY the supplied outputs.

DO NOT use outside knowledge.

DO NOT search the internet.

Evaluate confidence based on:

1. Completeness
2. Consistency
3. Evidence
4. Missing Information
5. Reviewer Feedback

Scoring Rules

95-100 = Excellent

85-94 = Very High

75-84 = High

60-74 = Medium

Below 60 = Low

If confidence is below 75,
recommend another analysis pass.

Return ONLY valid JSON.

Schema

{{
    "overall_confidence": 0,
    "analysis_confidence": 0,
    "summary_confidence": 0,
    "citation_confidence": 0,
    "insight_confidence": 0,
    "review_confidence": 0,
    "weak_sections": [],
    "recommendation": ""
}}

Analysis

{analysis}

Summary

{summary}

Citations

{citations}

Insights

{insights}

Review

{review}
"""

        result = super().run(
            prompt,
            ConfidenceOutput,
        )

        logger.info(
            f"Confidence Score: {result.overall_confidence}"
        )

        return result


confidence = ConfidenceAgent()