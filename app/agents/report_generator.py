from app.services.llm_service import llm_service
from app.services.logger_service import logger


class ReportGenerator:
    """
    Report Generator Agent

    Responsibilities
    ----------------
    • Generate the final professional Markdown report.
    • Use ONLY extracted information.
    • Never invent missing details.
    • Produce a publication-quality report.
    """

    def run(
        self,
        metadata: dict,
        analysis: dict,
        summary: dict,
        citations: dict,
        insights: dict,
        review: dict,
        fact_check: dict,
        hallucination: dict,
        confidence: dict,
    ):

        logger.info("Generating Final Report...")

        prompt = f"""
You are an expert technical writer.

Generate a professional research report in Markdown.

STRICT RULES

- Use ONLY the supplied information.
- NEVER invent:
  - datasets
  - experiments
  - results
  - references
  - citations
  - metrics
  - hyperparameters
  - implementation details
  - future work
  - applications

If information is missing, write:

"Not specified in the paper."

If results are unavailable:

"Not reported."

Produce a well-formatted report using the following sections.

# Research Report

## Paper Metadata

## Executive Summary

## Problem Statement

## Methodology

## Experiments

## Datasets

## Results

## Limitations

## Technical Summary

## Beginner Summary

## Key Insights

## Future Work

## Applications

## Citations

## References

## Fact Checking

## Hallucination Detection

## Confidence Assessment

## Review

## Conclusion

Metadata

{metadata}

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

Fact Checking

{fact_check}

Hallucination

{hallucination}

Confidence

{confidence}
"""

        response = llm_service.invoke(prompt)

        # -------------------------------
        # Convert Gemini response to string
        # -------------------------------

        markdown = ""

        if isinstance(response.content, str):

            markdown = response.content

        elif isinstance(response.content, list):

            parts = []

            for item in response.content:

                if isinstance(item, str):

                    parts.append(item)

                elif isinstance(item, dict):

                    if item.get("type") == "text":
                        parts.append(item.get("text", ""))

                elif hasattr(item, "text"):

                    parts.append(item.text)

            markdown = "\n".join(parts)

        else:

            markdown = str(response.content)

        logger.info("Final report generated successfully.")

        return {
            "markdown": markdown,
            "report_json": {
                "metadata": metadata,
                "analysis": analysis,
                "summary": summary,
                "citations": citations,
                "insights": insights,
                "review": review,
                "fact_check": fact_check,
                "hallucination": hallucination,
                "confidence": confidence,
            },
        }


report_generator = ReportGenerator()