from engine.utils.types import FileIO, Logger

def make_file_io(logger: Logger) -> FileIO:
    def read_file(path: str) -> str:
        logger.debug(f"Reading file from {path}")
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def write_file(path: str, text: str) -> None:
        logger.debug(f"Writing to {path}")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    
    return FileIO(
        read_file=read_file,
        write_file=write_file,
    )