from app.services.llm_service import llm_service
from app.services.logger_service import logger


class PlannerAgent:
    """
    Planner Agent

    Responsible for creating an execution plan
    before the workflow starts.

    It decides which agents should run
    depending on the uploaded research paper.
    """

    def run(self, paper: str):

        logger.info("Planning workflow...")

        prompt = f"""
You are the Planning Agent of an AI research assistant.

Your job is to decide which agents should execute.

Available agents:

1. metadata
2. analyzer
3. reviewer
4. summarizer
5. citation
6. insights
7. fact_checker
8. hallucination
9. confidence
10. report_generator
11. exporter

Rules

- Always start with metadata.
- Then analyzer.
- Then reviewer.
- Then summarizer.
- Then citation.
- Then insights.
- Then fact_checker.
- Then hallucination.
- Then confidence.
- Then report_generator.
- Then exporter.

Return ONLY valid JSON.

Example

{{
    "execution_plan":[
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
        "exporter"
    ]
}}

Paper

{paper}
"""

        response = llm_service.invoke(prompt)

        logger.info("Planning completed.")

        return response.content


planner = PlannerAgent()