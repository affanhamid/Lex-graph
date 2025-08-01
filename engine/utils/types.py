from dataclasses import dataclass
from typing import Callable

@dataclass(frozen=True)
class Logger:
    info: Callable[[str], None]
    warn: Callable[[str], None]
    debug: Callable[[str], None]
    error: Callable[[str], None]


@dataclass(frozen=True)
class FileIO:
    read_file: Callable[[str], str]
    write_file: Callable[[str, str], None]
