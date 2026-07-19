from app.agents.base_agent import BaseAgent
from app.models.outputs import AnalysisOutput
from app.prompts import ANALYZER_PROMPT
from app.services.logger_service import logger


class AnalyzerAgent(BaseAgent):
    """
    Analyzer Agent

    Responsibilities
    ----------------
    • Analyze the research paper
    • Extract only factual information
    • Never hallucinate
    • Return structured JSON
    """

    def run(self, paper: str):

        logger.info("Running Analyzer Agent...")

        prompt = f"""
{ANALYZER_PROMPT}

STRICT INSTRUCTIONS

Extract ONLY information explicitly available in the paper.

NEVER use outside knowledge.

NEVER guess.

NEVER infer.

NEVER fabricate any of the following:

- datasets
- experiments
- hyperparameters
- references
- implementation details
- training procedure
- software versions
- hardware specifications
- accuracy
- precision
- recall
- F1-score
- ROC
- AUC
- confusion matrix
- performance metrics
- statistical tests
- results
- conclusions
- future work
- limitations

Rules

If datasets are not mentioned:

"Not specified in the paper."

If experiments are missing:

"Not specified in the paper."

If results are missing:

"Not reported."

If limitations are missing:

"Not specified in the paper."

Keep every answer concise.

Return ONLY valid JSON.

Schema

{{
    "problem_statement": "",
    "methodology": "",
    "experiments": "",
    "datasets": [],
    "results": "",
    "limitations": ""
}}

Research Paper

{paper}
"""

        result = super().run(
            prompt,
            AnalysisOutput,
        )

        logger.info("Analyzer completed successfully.")

        return result


analyzer = AnalyzerAgent()