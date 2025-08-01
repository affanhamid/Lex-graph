import logging
from engine.utils.types import Logger


def make_logger(name: str = "lexgraph") -> Logger:
    log = logging.getLogger(name)
    if not log.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")
        handler.setFormatter(formatter)
        log.addHandler(handler)
        log.setLevel(logging.DEBUG)

    return Logger(
        debug=log.debug,
        info=log.info,
        warn=log.warn,
        error=log.error,
    )
