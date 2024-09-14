from nglcobdai_utils import get_logger


class TestLogger:
    @classmethod
    def setup_class(cls):
        cls.logger = get_logger(
            "test_logger", log_file="logs/test.log", is_stream=False
        )

    def test_logger_debug(self):
        self.logger.debug("debug")
        assert True

    def test_logger_info(self):
        self.logger.info("info")
        assert True

    def test_logger_warning(self):
        self.logger.warning("warning")
        assert True

    def test_logger_error(self):
        self.logger.error("error", exc_info=True)
        assert True

    def test_logger_critical(self):
        self.logger.critical("critical", exc_info=True)
        assert True

    def test_logger_exception(self):
        try:
            raise Exception("test exception")
        except Exception as e:
            self.logger.exception(e)

    def test_get_log_message(self):
        log_message = self.logger.get_log_message()
        assert log_message is not None
