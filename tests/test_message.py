from nglcobdai_utils import Message
import pytest


class TestMessage:
    @classmethod
    def setup_class(cls):
        cls.message = Message("sample/messages.test.ini")

    def test_message(self):
        """Test a normal message retrieval with correct section, key, and arguments."""
        gt = "This is a sample test message01 from Test in MESSAGE section."
        assert self.message("TEST", "MESSAGE01", first="Test", second="MESSAGE") == gt

    def test_message_notfound_section(self):
        """Test error handling when the specified section is not found in the message file."""
        with pytest.raises(ValueError) as e:
            _ = self.message("XXX", "MESSAGE01", first="Test", second="MESSAGE")
        assert str(e.value) == Message.ERROR_MESSAGE_SECTION_NOT_FOUND

    def test_message_notfound_key(self):
        """Test error handling when the specified key is not found in the given section."""
        with pytest.raises(ValueError) as e:
            _ = self.message("TEST", "XXX", first="Test", second="MESSAGE")
        assert str(e.value) == Message.ERROR_MESSAGE_KEY_NOT_FOUND

    def test_message_notfound_args(self):
        """Test error handling when required arguments for the message template are missing."""
        with pytest.raises(ValueError) as e:
            _ = self.message("TEST", "MESSAGE01")
        assert str(e.value) == Message.ERROR_MESSAGE_ARGS_MISSING

    def test_message_too_few_args(self):
        """Test error handling when only some of the required arguments are provided."""
        with pytest.raises(ValueError) as e:
            _ = self.message("TEST", "MESSAGE01", first="Test")
        assert str(e.value) == Message.ERROR_MESSAGE_ARGS_MISSING

    def test_message_too_many_args(self):
        """Test handling of extra arguments; message should ignore extra args without error."""
        gt = "This is a sample test message01 from Test in MESSAGE section."
        kargs = {"first": "Test", "second": "MESSAGE", "third": "XXX"}
        assert self.message("TEST", "MESSAGE01", **kargs) == gt


class TestMessageNoSectionFile:
    def test_message(self):
        """Test error handling when the message file is missing section headers."""
        with pytest.raises(ValueError) as e:
            _ = Message("sample/messages.test.nosection.ini")
        assert str(e.value) == Message.ERROR_MESSAGE_MISSING_SECTION_HEADER


class TestMessageNotFoundFile:
    def test_message(self):
        """Test error handling when the specified message file does not exist."""
        with pytest.raises(ValueError) as e:
            _ = Message("sample/messages.test.notfound.ini")
        assert str(e.value) == Message.ERROR_MESSAGE_FILE_NOT_FOUND
