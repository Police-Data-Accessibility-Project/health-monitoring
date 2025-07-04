"""
Logging logic for health-monitoring.
"""
import logging
import os
from logging.handlers import TimedRotatingFileHandler

from src.log.constants import LOG_FILENAME, LOGGER_NAME, WEEKLY_ON_MONDAY, HANDLER_SUFFIX, LOG_FORMAT


def setup_logger() -> logging.Logger:
    """
    Create a logger and set up a rotating file handler to log messages with timestamps and levels.
    """
    # Determine the parent directory of the script's directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)

    # Set the log path in the parent directory
    log_path = os.path.join(parent_dir, LOG_FILENAME)

    # Create a logger
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.INFO)

    # Create a handler that rotates logs weekly on Monday
    handler = TimedRotatingFileHandler(
        filename=log_path,
        when=WEEKLY_ON_MONDAY,
        backupCount=1
    )
    handler.suffix = HANDLER_SUFFIX

    # Create a formatter and set it for the handler
    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger