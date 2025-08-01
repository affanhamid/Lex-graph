from returns.result import Result as ReturnsResult, ResultE
from typing import TypeVar

T = TypeVar("T")
Result = ResultE[ReturnsResult[T, Exception]]
