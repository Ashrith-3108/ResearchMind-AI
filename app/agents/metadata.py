from app.agents.base_agent import BaseAgent
from app.models.metadata import MetadataOutput
from app.services.logger_service import logger
from app.services.chunk_service import chunk_service


METADATA_PROMPT = """
You are an expert research paper metadata extraction assistant.

Your task is to extract ONLY information explicitly present
in the research paper.

DO NOT GUESS.

DO NOT HALLUCINATE.

If any information is missing, return:

"Not specified in the paper."

Extract:

1. Title
2. Authors
3. Abstract
4. Keywords
5. Institution
6. Department
7. Publication Year
8. Conference / Journal
9. Domain
10. DOI
11. Email IDs

Return ONLY valid JSON.

Schema

{
    "title": "",
    "authors": [],
    "abstract": "",
    "keywords": [],
    "institution": "",
    "department": "",
    "year": "",
    "venue": "",
    "domain": "",
    "doi": "",
    "emails": []
}
"""


class MetadataAgent(BaseAgent):
    """
    Extract metadata from research paper.
    """

    def run(self, paper: str):

        logger.info("Running Metadata Agent...")

        # Use only a few chunks instead of the entire paper
        context = chunk_service.get_context(
            paper,
            max_chunks=3,
        )

        prompt = f"""
{METADATA_PROMPT}

Research Paper

{context}
"""

        result = super().run(
            prompt,
            MetadataOutput,
        )

        logger.info("Metadata extraction completed.")

        return result


metadata = MetadataAgent()