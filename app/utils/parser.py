import json
import re
from typing import Any, Dict, List

from app.services.logger_service import logger


class Parser:
    """
    Utility class for parsing LLM responses.

    Handles:
    - JSON extraction
    - Markdown cleanup
    - Code fence removal
    - Bullet extraction
    - Table extraction
    """

    # ==========================================================
    # EXTRACT JSON
    # ==========================================================

    def extract_json(
        self,
        text: str,
    ) -> Dict:

        if not text:
            return {}

        text = self.remove_markdown(text)

        try:

            return json.loads(text)

        except Exception:

            match = re.search(
                r"\{[\s\S]*\}",
                text,
            )

            if match:

                try:

                    return json.loads(match.group())

                except Exception:

                    logger.exception(
                        "Failed parsing JSON."
                    )

        return {}

    # ==========================================================
    # REMOVE MARKDOWN
    # ==========================================================

    def remove_markdown(
        self,
        text: str,
    ) -> str:

        if not text:
            return ""

        text = text.strip()

        text = re.sub(
            r"^```json",
            "",
            text,
            flags=re.MULTILINE,
        )

        text = re.sub(
            r"^```",
            "",
            text,
            flags=re.MULTILINE,
        )

        text = text.replace(
            "```",
            "",
        )

        return text.strip()

    # ==========================================================
    # EXTRACT BULLETS
    # ==========================================================

    def extract_bullets(
        self,
        text: str,
    ) -> List[str]:

        bullets = []

        for line in text.splitlines():

            line = line.strip()

            if line.startswith("- "):

                bullets.append(
                    line[2:].strip()
                )

            elif line.startswith("* "):

                bullets.append(
                    line[2:].strip()
                )

            elif re.match(
                r"^\d+\.",
                line,
            ):

                bullets.append(
                    re.sub(
                        r"^\d+\.\s*",
                        "",
                        line,
                    )
                )

        return bullets

    # ==========================================================
    # EXTRACT TABLES
    # ==========================================================

    def extract_tables(
        self,
        markdown: str,
    ) -> List[List[str]]:

        tables = []

        current = []

        for line in markdown.splitlines():

            if "|" in line:

                current.append(line)

            elif current:

                tables.append(current)

                current = []

        if current:

            tables.append(current)

        return tables

    # ==========================================================
    # CLEAN RESPONSE
    # ==========================================================

    def clean(
        self,
        text: str,
    ) -> str:

        text = self.remove_markdown(text)

        text = text.replace(
            "\r",
            "",
        )

        while "\n\n\n" in text:

            text = text.replace(
                "\n\n\n",
                "\n\n",
            )

        return text.strip()

    # ==========================================================
    # IS JSON
    # ==========================================================

    def is_json(
        self,
        text: str,
    ) -> bool:

        try:

            json.loads(
                self.remove_markdown(text)
            )

            return True

        except Exception:

            return False

    # ==========================================================
    # TO JSON STRING
    # ==========================================================

    def to_json(
        self,
        data: Any,
    ) -> str:

        return json.dumps(
            data,
            indent=4,
            ensure_ascii=False,
        )


parser = Parser()