from nglcobdai_utils import StringHandlerInfo, get_logger


class TestStringLogger:
    @classmethod
    def setup_class(cls):
        string_handler_info = StringHandlerInfo(log_level="DEBUG")
        cls.logger = get_logger(name="test_string_logger", sh_info=string_handler_info)

    def test_debug_logger(self):
        self.logger.debug("debug")
        print(self.logger.get_log_message())
        assert True

    def test_info_logger(self):
        self.logger.info("info")
        print(self.logger.get_log_message())
        assert True

    def test_warning_logger(self):
        self.logger.warning("warning")
        print(self.logger.get_log_message())
        assert True

    def test_error_logger(self):
        self.logger.error("error", exc_info=False)
        print(self.logger.get_log_message())
        assert True

    def test_critical_logger(self):
        self.logger.critical("critical", exc_info=False)
        print(self.logger.get_log_message())
        assert True

    def test_exception_logger(self):
        try:
            raise Exception("test exception")
        except Exception as e:
            self.logger.exception(e)
        print(self.logger.get_log_message())
        assert True
