import pytest

from nglcobdai_utils import TemplateError


class TestTemplateError:
    def test_default_message(self):
        """Test default error message format with no arguments."""

        with pytest.raises(TemplateError) as e:
            raise TemplateError()
        assert str(e.value) == TemplateError().message
