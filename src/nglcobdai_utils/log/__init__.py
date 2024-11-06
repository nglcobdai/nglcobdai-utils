import logging

from nglcobdai_utils.log.handler import (
    ConsoleHandlerInfo,
    FileHandlerInfo,
    HandlerInfo,
    RotatingFileHandlerInfo,
    StringHandlerInfo,
    TimedRotatingFileHandlerInfo,
)
from nglcobdai_utils.log.logger import CustomLogger

logger = None


def get_logger(
    name,
    ch_info=ConsoleHandlerInfo(is_use=False),
    fh_info=FileHandlerInfo(is_use=False),
    sh_info=StringHandlerInfo(is_use=False),
):
    """Retrieve a configured logger.

    Args:
        name (str): The name of the logger.
        ch_info (ConsoleHandlerInfo, optional): Console handler information (default: ConsoleHandlerInfo(is_use=False)).
        fh_info (FileHandlerInfo | RotatingFileHandlerInfo | TimedRotatingFileHandlerInfo, optional): \
            File handler information (default: FileHandlerInfo(is_use=False)).
        sh_info (StringHandlerInfo, optional): String handler information (default: StringHandlerInfo(is_use=False)).

    Example:
        >>> console_handler_info = ConsoleHandlerInfo(log_level="INFO")
        >>> file_handler_info = FileHandlerInfo(log_level="DEBUG", filename="~/logs/test.log")
        >>> string_handler_info = StringHandlerInfo(log_level="DEBUG")
        >>> logger = get_logger(
        ...     name="test_logger",
        ...     ch_info=console_handler_info,
        ...     fh_info=file_handler_info,
        ...     sh_info=string_handler_info,
        ... )

    Returns:
        logging.Logger: The configured logger instance.
    """
    logging.setLoggerClass(CustomLogger)
    _logger = logging.getLogger(name)
    _logger.settting_logger(ch_info, fh_info, sh_info)
    return _logger


def set_logger(
    name,
    ch_info=ConsoleHandlerInfo(is_use=False),
    fh_info=FileHandlerInfo(is_use=False),
    sh_info=StringHandlerInfo(is_use=False),
):
    """Set a configured logger.

    Args:
        name (str): The name of the logger.
        ch_info (ConsoleHandlerInfo, optional): Console handler information (default: ConsoleHandlerInfo(is_use=False)).
        fh_info (FileHandlerInfo | RotatingFileHandlerInfo | TimedRotatingFileHandlerInfo, optional): \
            File handler information (default: FileHandlerInfo(is_use=False)).
        sh_info (StringHandlerInfo, optional): String handler information (default: StringHandlerInfo(is_use=False)).

    Example:
        >>> console_handler_info = ConsoleHandlerInfo(log_level="INFO")
        >>> file_handler_info = FileHandlerInfo(log_level="DEBUG", filename="~/logs/test.log")
        >>> string_handler_info = StringHandlerInfo(log_level="DEBUG")
        >>> set_logger(
        ...     name="test_logger",
        ...     ch_info=console_handler_info,
        ...     fh_info=file_handler_info,
        ...     sh_info=string_handler_info,
        ... )

    Returns:
        logging.Logger: The configured logger instance.
    """
    global logger
    logger = get_logger(name, ch_info, fh_info, sh_info)
    logger.settting_logger(ch_info, fh_info, sh_info)
