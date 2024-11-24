import pytest

from nglcobdai_utils import (
    ConsoleHandlerInfo,
    StringHandlerInfo,
    TemplateError,
    logging,
    set_logger,
)


class TestTemplateError:
    def test_default_message(self):
        """Test default error message format with no arguments."""

        with pytest.raises(TemplateError) as e:
            raise TemplateError()
        assert str(e.value) == TemplateError().message


class SampleError(TemplateError):
    _CODE = "SAMPLE_ERROR"
    _NOTE = "This is a {arg} error."


class TestSampleError:

    def test_default_message(self):
        """Test default error message format with no arguments."""

        with pytest.raises(SampleError) as e:
            raise SampleError(arg="sample")
        assert str(e.value) == "SAMPLE_ERROR: This is a sample error."


class TestLoggingTemplateError:
    @classmethod
    def setup_class(cls):
        string_handler_info = StringHandlerInfo(log_level="DEBUG")
        console_handler_info = ConsoleHandlerInfo(log_level="DEBUG")
        set_logger(
            name="test_template_error",
            sh_info=string_handler_info,
            ch_info=console_handler_info,
        )

    def test_logging_template_error(self):
        with pytest.raises(TemplateError):
            raise TemplateError()

        assert logging.logger.name == "test_template_error"
        assert logging.logger.get_log_message() != ""
