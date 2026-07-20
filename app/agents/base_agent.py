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

            # OpenAI / OpenRouter
            if isinstance(response.content, str):

                raw = response.content.strip()

            # Gemini
            elif isinstance(response.content, list):

                texts = []

                for part in response.content:

                    if isinstance(part, str):

                        texts.append(part)

                    elif hasattr(part, "text"):

                        texts.append(part.text)

                    else:

                        texts.append(str(part))

                raw = "\n".join(texts).strip()

            else:

                raw = str(response.content).strip()

        if not raw:

            logger.error("LLM returned an empty response.")

            raise ValueError(
                "LLM returned an empty response."
            )

        logger.info("LLM Response Received")

        logger.info(raw[:1000])

        try:

            result = parser.parse(raw)

            logger.info("Successfully parsed LLM response.")

            return result

        except Exception as e:

            logger.exception("Failed to parse LLM response.")

            logger.error(raw)

            raise e