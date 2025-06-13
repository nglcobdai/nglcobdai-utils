import logging
from datetime import datetime
from logging import DEBUG, INFO, FileHandler, Formatter, StreamHandler
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

import pytz

from nglcobdai_utils.log.handler import (
    FileHandlerInfo,
    RotatingFileHandlerInfo,
    StringLogHandler,
    TimedRotatingFileHandlerInfo,
)


class CustomLogger(logging.Logger):
    def __init__(self, name):
        """Constructor of CustomLogger

        Args:
            name (str): Name of the logger.
        """
        super().__init__(name)
        self.jst = pytz.timezone("Asia/Tokyo")
        self.string_handler = None
        self.setLevel(DEBUG)

    def _jst_time(self, *args):
        """Get Japan Standard Time

        Returns:
            time.struct_time: JST
        """
        return datetime.now(self.jst).timetuple()

    def settting_logger(self, ch_info, fh_info, sh_info):
        """Set logger

        Args:
            ch_info (ConsoleHandlerInfo): Console handler information.
            fh_info (FileHandlerInfo | RotatingFileHandlerInfo | TimedRotatingFileHandlerInfo): \
                File handler information.
            sh_info (StringHandlerInfo): String handler information.
        """
        if ch_info.is_use:
            self._set_console_handler(ch_info)

        if fh_info.is_use:
            self._set_file_handler(fh_info)

        if sh_info.is_use:
            self._set_string_handler(sh_info)

    def _decode_handler_info(self, handler_info):
        """Decode handler information

        Args:
            handler_info (HandlerInfo): Handler information.

        Returns:
            numeric_level (int): Numeric level
            formatter (logging.Formatter): Formatter
        """
        numeric_level = getattr(logging, handler_info.log_level, INFO)

        formatter = Formatter(handler_info.format)
        formatter.converter = self._jst_time

        return numeric_level, formatter

    def _set_console_handler(self, handler_info):
        """Set console handler

        Args:
            handler_info (ConsoleHandlerInfo): Console handler information.
        """
        numeric_level, formatter = self._decode_handler_info(handler_info)

        console_handler = StreamHandler()
        console_handler.setLevel(numeric_level)
        console_handler.setFormatter(formatter)
        self.addHandler(console_handler)

    def _set_file_handler(self, handler_info):
        """Set console handler

        Args:
            handler_info (FileHandlerInfo | RotatingFileHandlerInfo | TimedRotatingFileHandlerInfo): \
                File handler information.
        """
        numeric_level, formatter = self._decode_handler_info(handler_info)
        handler_info.filename.parent.mkdir(parents=True, exist_ok=True)

        if type(handler_info) is FileHandlerInfo:
            file_handler = FileHandler(**handler_info.get_param())
        elif type(handler_info) is RotatingFileHandlerInfo:
            file_handler = RotatingFileHandler(**handler_info.get_param())
        elif type(handler_info) is TimedRotatingFileHandlerInfo:
            file_handler = TimedRotatingFileHandler(**handler_info.get_param())

        file_handler.setLevel(numeric_level)
        file_handler.setFormatter(formatter)
        self.addHandler(file_handler)

    def _set_string_handler(self, handler_info):
        """Set console handler

        Args:
            handler_info (StringHandlerInfo): String handler information.
        """
        numeric_level, formatter = self._decode_handler_info(handler_info)

        self.string_handler = StringLogHandler()
        self.string_handler.setLevel(numeric_level)
        self.string_handler.setFormatter(formatter)
        self.addHandler(self.string_handler)

    def get_log_message(self):
        """Get last log message"""
        if not self.string_handler:
            self.warning("String handler is not set.")
            return ""

        return self.string_handler.get_log_message()
