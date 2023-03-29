"""Arrrgs log utils"""
from logging import Formatter, Logger, StreamHandler, getLogger


def get_logger(name: str) -> Logger:
    """Return a logger with the specified name."""
    log = getLogger(name)
    stream_handler = StreamHandler()
    stream_handler.setFormatter(Formatter(
        "%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
    ))
    log.addHandler(stream_handler)
    return log
