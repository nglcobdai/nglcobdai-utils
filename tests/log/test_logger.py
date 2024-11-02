from nglcobdai_utils import get_logger


class TestDefaultLogger:
    @classmethod
    def setup_class(cls):
        cls.logger = get_logger(name="test_default_logger")

    def test_debug_logger(self):
        self.logger.debug("debug")
        assert True

    def test_info_logger(self):
        self.logger.info("info")
        assert True

    def test_warning_logger(self):
        self.logger.warning("warning")
        assert True

    def test_error_logger(self):
        self.logger.error("error", exc_info=False)
        assert True

    def test_critical_logger(self):
        self.logger.critical("critical", exc_info=False)
        assert True

    def test_exception_logger(self):
        try:
            raise Exception("test exception")
        except Exception as e:
            self.logger.exception(e)
        assert True
