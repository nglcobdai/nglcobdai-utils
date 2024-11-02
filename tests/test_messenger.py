from nglcobdai_utils import Messenger
import pytest


class TestMessenger:
    @classmethod
    def setup_class(cls):
        cls.messenger = Messenger("sample/messages.test.ini")

    def test_messenger(self):
        """Test a normal message retrieval with correct section, key, and arguments."""
        gt = "This is a sample test message01 from Test in MESSAGE section."
        assert self.messenger("TEST", "MESSAGE01", first="Test", second="MESSAGE") == gt

    def test_messenger_notfound_section(self):
        """Test error handling when the specified section is not found in the message file."""
        with pytest.raises(ValueError) as e:
            _ = self.messenger("XXX", "MESSAGE01", first="Test", second="MESSAGE")
        assert str(e.value) == Messenger.ERROR_MESSAGE_SECTION_NOT_FOUND

    def test_messenger_notfound_key(self):
        """Test error handling when the specified key is not found in the given section."""
        with pytest.raises(ValueError) as e:
            _ = self.messenger("TEST", "XXX", first="Test", second="MESSAGE")
        assert str(e.value) == Messenger.ERROR_MESSAGE_KEY_NOT_FOUND

    def test_messenger_notfound_args(self):
        """Test error handling when required arguments for the message template are missing."""
        with pytest.raises(ValueError) as e:
            _ = self.messenger("TEST", "MESSAGE01")
        assert str(e.value) == Messenger.ERROR_MESSAGE_ARGS_MISSING

    def test_messenger_too_few_args(self):
        """Test error handling when only some of the required arguments are provided."""
        with pytest.raises(ValueError) as e:
            _ = self.messenger("TEST", "MESSAGE01", first="Test")
        assert str(e.value) == Messenger.ERROR_MESSAGE_ARGS_MISSING

    def test_messenger_too_many_args(self):
        """Test handling of extra arguments; message should ignore extra args without error."""
        gt = "This is a sample test message01 from Test in MESSAGE section."
        kargs = {"first": "Test", "second": "MESSAGE", "third": "XXX"}
        assert self.messenger("TEST", "MESSAGE01", **kargs) == gt


class TestMessengerNoSectionFile:
    def test_messenger_nosection(self):
        """Test error handling when the message file is missing section headers."""
        with pytest.raises(ValueError) as e:
            _ = Messenger("sample/messages.test.nosection.ini")
        assert str(e.value) == Messenger.ERROR_MESSAGE_MISSING_SECTION_HEADER


class TestMessengerNotFoundFile:
    def test_messenger_notfound(self):
        """Test error handling when the specified message file does not exist."""
        with pytest.raises(ValueError) as e:
            _ = Messenger("sample/messages.test.notfound.ini")
        assert str(e.value) == Messenger.ERROR_MESSAGE_FILE_NOT_FOUND
