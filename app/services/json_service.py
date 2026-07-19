import json
from pathlib import Path

from app.services.logger_service import logger


class JSONService:
    """
    JSON Service

    Responsibilities
    ----------------
    • Save JSON reports
    • Load JSON reports
    • Pretty print JSON
    • Validate JSON
    """

    def save(
        self,
        data: dict,
        output_path,
    ) -> str:

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(
            output_path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

        logger.info(
            f"JSON saved -> {output_path}"
        )

        return str(output_path)

    def load(
        self,
        file_path,
    ) -> dict:

        file_path = Path(file_path)

        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(file)

    def pretty(
        self,
        data: dict,
    ) -> str:

        return json.dumps(
            data,
            indent=4,
            ensure_ascii=False,
        )

    def validate(
        self,
        file_path,
    ) -> bool:

        try:

            self.load(file_path)

            return True

        except Exception as e:

            logger.error(
                f"Invalid JSON: {e}"
            )

            return False


json_service = JSONService()