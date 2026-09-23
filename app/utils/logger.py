import logging
from pathlib import Path

from app.config import settings


LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "insightagent.log"


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    level = getattr(
        logging,
        settings.LOG_LEVEL.upper(),
        logging.INFO,
    )

    logger.setLevel(level)

    # Create logs directory
    LOG_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    formatter = logging.Formatter(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    )

    # Terminal logging
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File logging
    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger