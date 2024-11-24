import pytest

from nglcobdai_utils import TemplateError


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
