import logging
import os
from datetime import datetime
from logging import DEBUG, FileHandler, Formatter, StreamHandler, getLogger
from time import time

import pytz


class Logger:
    def __init__(self, name, log_file=None):
        """Constructor of Logger

        Args:
            name (str): Name of the logger.
            log_file (str, optional): File name of the log(None).
        """
        self.logger = getLogger(name)

        log_level = os.getenv("LOGGING_LEVEL", "DEBUG").upper()
        numeric_level = getattr(logging, log_level, DEBUG)

        self.jst = pytz.timezone("Asia/Tokyo")

        if log_file is None:
            log_file = time().strftime("%Y%m%d%H%M%S") + ".log"

        self._set_logger(numeric_level, log_file)

    def _jst_time(self):
        """Get Japan Standard Time

        Returns:
            time.struct_time: JST
        """
        return datetime.now(self.jst).timetuple()

    def _set_logger(self, numeric_level, log_file):
        """Set logger

        Args:
            numeric_level (int): Numeric level of the logger.
            log_file (str): File name of the log.
        """
        self.logger.setLevel(numeric_level)

        # Set console handler
        console_handler = StreamHandler()
        formatter = Formatter(
            "%(asctime)s : %(levelname)s : %(filename)s - %(message)s"
        )
        formatter.converter = self._jst_time  # Translate UTC to JST
        console_handler.setFormatter(formatter)

        # Set file handler
        file_handler = FileHandler(log_file)
        file_handler.setFormatter(formatter)

        # If the logger has no handlers, add console handler and file handler
        if not self.logger.hasHandlers():
            # ロガーにコンソールハンドラとファイルハンドラを追加
            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)
