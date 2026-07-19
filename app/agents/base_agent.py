from langchain_core.output_parsers import PydanticOutputParser

from app.services.llm_service import llm_service
from app.services.logger_service import logger


class BaseAgent:

    def run(
        self,
        prompt: str,
        output_model,
    ):

        parser = PydanticOutputParser(
            pydantic_object=output_model
        )

        final_prompt = f"""
{prompt}

IMPORTANT

Return ONLY valid JSON.

Do not explain.

Do not wrap the JSON inside markdown.

{parser.get_format_instructions()}
"""

        logger.info("Sending prompt to LLM...")

        response = llm_service.invoke(final_prompt)

        raw = ""

        if hasattr(response, "content"):

            raw = response.content.strip()

        if not raw:

            logger.error("LLM returned an empty response.")

            raise ValueError(
                "LLM returned an empty response."
            )

        logger.info("LLM Response Received")

        logger.info(raw[:1000])

        try:

            return parser.parse(raw)

        except Exception as e:

            logger.exception("Failed to parse LLM response.")

            logger.error(raw)

            raise e