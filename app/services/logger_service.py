import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from app.config import settings


class LoggerService:
    """
    Centralized logging service.
    """

    def __init__(self):

        log_dir = Path(settings.LOG_DIR)
        log_dir.mkdir(parents=True, exist_ok=True)

        self.logger = logging.getLogger("ResearchMind")

        if self.logger.handlers:
            return

        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = RotatingFileHandler(
            log_dir / "researchmind.log",
            maxBytes=5 * 1024 * 1024,
            backupCount=5,
            encoding="utf-8",
        )

        console_handler = logging.StreamHandler()

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def exception(self, message):
        self.logger.exception(message)

    def debug(self, message):
        self.logger.debug(message)


logger = LoggerService()