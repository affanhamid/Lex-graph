import traceback
from returns.result import Result, Failure, Success

def safe(func):
    def wrapper(*args, **kwargs) -> Result:
        try:
            return Success(func(*args, **kwargs))
        except Exception as e:
            tb = traceback.format_exc()
            return Failure(Exception(f"{str(e)}\nTraceback:\n{tb}"))
    return wrapper
