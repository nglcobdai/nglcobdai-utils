import datetime as dt
import logging
from datetime import datetime
from pathlib import Path

from pydantic import BaseModel


class StringLogHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.message = ""

    def emit(self, record):
        """Emit log

        Args:
            record (logging.LogRecord): Log record
        """
        self.message = self.format(record)

    def get_log_message(self):
        """Get last log message"""
        return self.message


class HandlerInfo(BaseModel):
    """Handler information

    Args:
        is_use (bool): Whether to use the handler.
        log_level (str): Log level.
        format (str): Log format.
            (default: `"%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s"`)
    """

    is_use: bool = True
    log_level: str = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format: str = (
        "%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s"
    )

    def get_param(self):
        """Get handler parameters

        Returns:
            Dict: Handler parameters
        """
        return (
            self.model_dump(exclude={"is_use", "log_level", "format"})
            if self.is_use
            else {}
        )


class ConsoleHandlerInfo(HandlerInfo):
    """Console handler information

    Args:
        format (str, optional): Log format. (default: `"%(asctime)s : %(levelname)s : %(filename)s - %(message)s"`)
    """

    format: str = "%(asctime)s : %(levelname)s : %(filename)s - %(message)s"


class FileHandlerInfo(HandlerInfo):
    """File handler information

    Args:
        filename (str | pathlib.Path, optional): Path of the log file. (default: `"~/logs/test.log"`)
        encoding (str, optional): Encoding of the log file. (default: `"utf-8"`)
    """

    filename: str | Path = Path("~/logs/default.log").expanduser()
    encoding: str = "utf-8"

    def __init__(self, **data):
        super().__init__(**data)
        if isinstance(self.filename, str):
            self.filename = Path(self.filename)


class TimedRotatingFileHandlerInfo(FileHandlerInfo):
    """Time rotating file handler information

    Args:
        backupCount (int): Number of backup files. (default: `5`)
        when (str): Type of interval. (default: `"D"`)
        interval (int): Interval of rotation. (default: `1`)
        atTime (datetime.time): JTC time to rotate. (default: `datetime.time(0, 0, 0)`)
        utc (bool): Whether to use UTC time. (default: `False`)
    """

    backupCount: int = 5
    when: str = "D"  # S, M, H, D, midnight
    interval: int = 1
    atTime: dt.time = dt.time(0, 0, 0)
    utc: bool = False


class RotatingFileHandlerInfo(FileHandlerInfo):
    """Rotating file handler information

    Args:
        backupCount (int): Number of backup files. (default: `5`)
        maxBytes (int): Maximum size of the log file. (default: `10485760`)
    """

    backupCount: int = 5
    maxBytes: int = 10485760  # 10MB


class StringHandlerInfo(HandlerInfo):
    """String handler information"""

    pass
