# from nglcobdai_utils import logger as log
from nglcobdai_utils import logging


class TestSetLogger:
    @classmethod
    def setup_class(cls):
        logging.set_logger(name="test set logger")

    def test_set_logger(self):
        assert logging.logger is not None
        assert logging.logger.name == "test set logger"
