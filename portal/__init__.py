import sys
import logging
import colorlog
import structlog


logging.getLogger("selenium").setLevel(logging.WARNING)
logging.getLogger("selenium.webdriver.remote.remote_connection").setLevel(
    logging.WARNING
)
logging.getLogger("requests").setLevel(logging.WARNING)


def BasicColorLogger(name="portal"):

    stdout = colorlog.StreamHandler()
    stdout.setFormatter(
        colorlog.ColoredFormatter(
            "%(name)s: %(white)s%(asctime)s%(reset)s | %(log_color)s%(levelname)s%(reset)s | %(blue)s%(filename)s:%(lineno)s%(reset)s >>> %(log_color)s%(message)s%(reset)s"
        )
    )

    logger = logging.getLogger(name)
    logger.handlers.clear()
    logger.addHandler(stdout)
    logger.propagate = False

    logging.basicConfig(level=logging.INFO)
    return logger


def Logger(name=None):
    structlog.stdlib.recreate_defaults()
    logging.basicConfig(level=logging.INFO)
    return structlog.get_logger(name)
