from dataclasses import dataclass
from typing import Callable

from engine.types import Result

@dataclass(frozen=True)
class Preprocessor:
    preprocess: Callable[[str], Result[str]]
