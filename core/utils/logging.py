# core/utils/logging.py

import logging

def setup_logging(log_file="game.log", log_level=logging.INFO):
    """
    Sets up logging to a file and the console.

    Args:
        log_file: The name of the log file.
        log_level: The logging level (e.g., logging.DEBUG, logging.INFO, logging.ERROR).
    """

    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # Create file handler and set level
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)

    # Create console handler and set level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Create formatter and add it to handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
