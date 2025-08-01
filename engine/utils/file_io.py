from engine.utils.error_handling import safe
from engine.utils.types import IO, Logger

def make_file_io(logger: Logger) -> IO:
    @safe
    def read_file(path: str):
        logger.debug(f"Reading file from {path}")
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    @safe
    def write_file(path: str, text: str):
        logger.debug(f"Writing to {path}")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    
    return IO(
        read=read_file,
        write=write_file,
    )
