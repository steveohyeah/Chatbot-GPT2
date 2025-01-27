import logging


# Logging configuration
def log_conf():
    """Function that returns the log object"""
    logging.basicConfig(
        filename="chatbot_logs.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger(__name__)
