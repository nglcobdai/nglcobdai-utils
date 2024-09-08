import logging
import os
from datetime import datetime
from logging import DEBUG, FileHandler, Formatter, StreamHandler, getLogger

import pytz


class Logger:
    def __init__(self, name, log_file=None):
        """Constructor of Logger

        Args:
            name (str): Name of the logger.
            log_file (str, optional): File name of the log(None).
        """
        self.logger = getLogger(name)
        self.jst = pytz.timezone("Asia/Tokyo")
        self._set_logger(log_file)

    def _jst_time(self, *args):
        """Get Japan Standard Time

        Returns:
            time.struct_time: JST
        """
        return datetime.now(self.jst).timetuple()

    def _set_logger(self, log_file):
        """Set logger

        Args:
            log_file (str): File name of the log.
        """
        log_level = os.getenv("LOGGING_LEVEL", "DEBUG").upper()
        numeric_level = getattr(logging, log_level, DEBUG)
        self.logger.setLevel(numeric_level)

        _format = "%(asctime)s : %(levelname)s : %(filename)s - %(message)s"
        formatter = Formatter(_format)
        formatter.converter = self._jst_time  # Translate UTC to JST

        if not self.logger.hasHandlers():
            self._set_console_handler(formatter)
            self._set_file_handler(log_file, formatter)

    def _set_console_handler(self, formatter):
        """Set console handler

        Args:
            formatter (logging.Formatter): Formatter
        """
        console_handler = StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def _set_file_handler(self, log_file, formatter):
        """Set file handler

        Args:
            log_file (str): File name of the log.
        """
        file_handler = FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
