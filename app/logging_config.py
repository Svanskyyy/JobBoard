import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def configure_logging(app):
    log_directory = (
        Path(app.root_path).parent
        / "logs"
    )

    log_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    log_file = (
        log_directory
        / "jobboard.log"
    )

    log_file_path = log_file.resolve()

    already_configured = any(
        isinstance(handler, RotatingFileHandler)
        and Path(handler.baseFilename).resolve()
        == log_file_path
        for handler in app.logger.handlers
    )

    if already_configured:
        return

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8",
    )

    file_handler.setLevel(
        logging.INFO
    )

    formatter = logging.Formatter(
        "%(asctime)s "
        "%(levelname)s "
        "%(message)s"
    )

    file_handler.setFormatter(
        formatter
    )

    app.logger.addHandler(
        file_handler
    )

    app.logger.setLevel(
        logging.INFO
    )

    app.logger.info(
        "JobBoard application started."
    )