import logging

from returns.result import safe
from engine.types import Result
from engine.utils.types import Logger

def make_logger(name: str = "lexgraph") -> Logger:
    log = logging.getLogger(name)
    if not log.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")
        handler.setFormatter(formatter)
        log.addHandler(handler)
        log.setLevel(logging.DEBUG)

    @safe
    def log_debug(message: str) -> Result[None]:
        log.debug(message)
    
    @safe
    def log_info(message: str) -> Result[None]:
        log.info(message)
    
    @safe
    def log_warn(message: str) -> Result[None]:
        log.warning(message)
    
    @safe
    def log_error(message: str) -> Result[None]:
        log.error(message)

    return Logger(
        debug=log_debug,
        info=log_info,
        warn=log_warn,
        error=log_error,
    )
