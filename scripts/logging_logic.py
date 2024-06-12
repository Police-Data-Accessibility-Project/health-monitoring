"""
Logging logic for health-monitoring.
"""
import logging
import os
from logging.handlers import TimedRotatingFileHandler


def setup_logger() -> logging.Logger:
    """
    Create a logger and set up a rotating file handler to log messages with timestamps and levels.
    """
    # Determine the parent directory of the script's directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)

    # Set the log path in the parent directory
    log_path = os.path.join(parent_dir, "health_monitoring.log")

    # Create a logger
    logger = logging.getLogger("HourlyLogger")
    logger.setLevel(logging.INFO)

    # Create a handler that rotates logs every day
    handler = TimedRotatingFileHandler(log_path, when="midnight", interval=1, backupCount=1)
    handler.suffix = "%Y-%m-%d"

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger