import json

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

Do not wrap JSON inside markdown.

{parser.get_format_instructions()}
"""

        logger.info("Sending prompt to LLM...")

        response = llm_service.invoke(final_prompt)

        raw = ""

        if hasattr(response, "content"):

            content = response.content

            # OpenAI response
            if isinstance(content, str):

                raw = content.strip()

            # Gemini response
            elif isinstance(content, list):

                texts = []

                for item in content:

                    if isinstance(item, str):

                        texts.append(item)

                    elif isinstance(item, dict):

                        # Gemini returns:
                        # {'type':'text','text':'{...json...}'}

                        if item.get("type") == "text":
                            texts.append(item.get("text", ""))

                    elif hasattr(item, "text"):

                        texts.append(item.text)

                    else:

                        texts.append(str(item))

                raw = "\n".join(texts).strip()

            else:

                raw = str(content).strip()

        if not raw:

            raise ValueError("LLM returned empty response.")

        logger.info("Raw LLM Output:")
        logger.info(raw[:1500])

        # Remove markdown if model returned it
        if raw.startswith("```json"):

            raw = raw.replace("```json", "").replace("```", "").strip()

        elif raw.startswith("```"):

            raw = raw.replace("```", "").strip()

        # Sometimes Gemini double-encodes JSON
        try:

            obj = json.loads(raw)

            if isinstance(obj, str):

                raw = obj

        except Exception:

            pass

        try:

            return parser.parse(raw)

        except Exception:

            logger.exception("Failed to parse JSON")

            print(raw)

            raise