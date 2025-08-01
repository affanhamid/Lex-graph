from dataclasses import dataclass
from typing import Callable
from engine.types import Result

@dataclass(frozen=True)
class Logger:
    info: Callable[[str], Result[None]]
    warn: Callable[[str], Result[None]]
    debug: Callable[[str], Result[None]]
    error: Callable[[str], Result[None]]


@dataclass(frozen=True)
class IO:
    read: Callable[[str], Result[str]]
    write: Callable[[str, str], Result[None]]
