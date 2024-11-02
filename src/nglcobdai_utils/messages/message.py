from string import Template
from configparser import (
    ConfigParser,
    NoSectionError,
    NoOptionError,
    MissingSectionHeaderError,
)
from pathlib import Path


class Message:
    """Message class to retrieve messages from a message file.

    Attributes:
        ERROR_MESSAGE_FILE_NOT_FOUND (str): Error message for missing message file.
        ERROR_MESSAGE_MISSING_SECTION_HEADER (str): Error message for missing section header in the message file.
        ERROR_MESSAGE_SECTION_NOT_FOUND (str): Error message for missing section in the message file.
        ERROR_MESSAGE_KEY_NOT_FOUND (str): Error message for missing key in the message file.
        ERROR_MESSAGE_UNEXPECTED (str): Error message for unexpected error while retrieving message.
        ERROR_MESSAGE_ARGS_MISSING (str): Error message for missing arguments in the message template.
    """

    ERROR_MESSAGE_FILE_NOT_FOUND = "The message file could not be found. \
            Please check the file path and try again."
    ERROR_MESSAGE_MISSING_SECTION_HEADER = "The message file is missing a required section header. \
        Please add the section header [XXX] to resolve this issue."
    ERROR_MESSAGE_SECTION_NOT_FOUND = "The specified message section could not be found. \
        Ensure the section name is correct or add the section if missing."
    ERROR_MESSAGE_KEY_NOT_FOUND = "The specified message code could not be found. \
        Verify the key name or add it to the relevant section in the file."
    ERROR_MESSAGE_UNEXPECTED = "An unexpected error occurred while retrieving the message. \
        Please review the file format and content for any irregularities."
    ERROR_MESSAGE_ARGS_MISSING = "Some required arguments are missing from the template. \
        Please provide all necessary arguments and try again."

    def __init__(self, filepath: str | Path) -> None:
        """Constructor of Message

        Args:
            filepath (str | Path): File path of the message file.
        """
        filepath = Path(filepath) if isinstance(filepath, str) else filepath
        self.messages = self._load(filepath)

    @staticmethod
    def _load(filepath: Path) -> ConfigParser:
        """Load message file

        Args:
            filepath (Path): File path of the message file.

        Returns:
            ConfigParser: Message file

        Raises:
            ValueError: If the file is not found or if the file is missing section
        """
        if not filepath.exists():
            raise ValueError(Message.ERROR_MESSAGE_FILE_NOT_FOUND)

        try:
            config = ConfigParser()
            config.read(str(filepath), encoding="utf-8")
            return config
        except MissingSectionHeaderError:
            raise ValueError(Message.ERROR_MESSAGE_MISSING_SECTION_HEADER)

    def __call__(self, section: str, key: str, **kwargs) -> str:
        """Get message

        Args:
            key (str): Key of the message.
            section (str): Section of the message.
            kwargs (dict): Arguments for message.

        Returns:
            str: Message

        Raises:
            ValueError: If message section or key is not found, or if required arguments are missing.
        """
        template = self._message(section, key)
        try:
            return Template(template).substitute(**kwargs)
        except KeyError:
            raise ValueError(self.ERROR_MESSAGE_ARGS_MISSING)

    def _message(self, section: str, key: str) -> str:
        """Get message string from section and key

        Args:
            key (str): Key
            section (str): Section

        Returns:
            str: Message

        Raises:
            ValueError: If message section or key is not found

        """
        try:
            return self.messages.get(section, key)
        except NoSectionError:
            raise ValueError(self.ERROR_MESSAGE_SECTION_NOT_FOUND)
        except NoOptionError:
            raise ValueError(self.ERROR_MESSAGE_KEY_NOT_FOUND)
        except Exception:
            raise ValueError(self.ERROR_MESSAGE_UNEXPECTED)
