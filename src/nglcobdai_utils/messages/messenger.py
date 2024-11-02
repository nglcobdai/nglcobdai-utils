from string import Template
from configparser import (
    ConfigParser,
    NoSectionError,
    NoOptionError,
    MissingSectionHeaderError,
)
from pathlib import Path


class Messenger:
    """Messenger class to retrieve messages from a message file."""

    ERROR_MESSAGE_FILE_NOT_FOUND = (
        "The message file could not be found. "
        "Please check the file path and try again."
    )
    """str: Error message displayed when the message file is missing."""

    ERROR_MESSAGE_MISSING_SECTION_HEADER = (
        "The message file is missing a required section header. "
        "Please add the section header [XXX] to resolve this issue."
    )
    """str: Error message for missing section header in the message file."""

    ERROR_MESSAGE_SECTION_NOT_FOUND = (
        "The specified message section could not be found. "
        "Ensure the section name is correct or add the section if missing."
    )
    """str: Error message displayed when the message section is missing."""

    ERROR_MESSAGE_KEY_NOT_FOUND = (
        "The specified message code could not be found. "
        "Verify the key name or add it to the relevant section in the file."
    )
    """str: Error message displayed when the specified message key is not found."""

    ERROR_MESSAGE_UNEXPECTED = (
        "An unexpected error occurred while retrieving the message. "
        "Please review the file format and content for any irregularities."
    )
    """str: Error message displayed when an unexpected error occurs."""

    ERROR_MESSAGE_ARGS_MISSING = (
        "Some required arguments are missing from the template. "
        "Please provide all necessary arguments and try again."
    )
    """str: Error message displayed when arguments are missing in the template."""

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
            raise ValueError(Messenger.ERROR_MESSAGE_FILE_NOT_FOUND)

        try:
            config = ConfigParser()
            config.read(str(filepath), encoding="utf-8")
            return config
        except MissingSectionHeaderError:
            raise ValueError(Messenger.ERROR_MESSAGE_MISSING_SECTION_HEADER)

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
        template = self._template(self.messages, section, key)
        message = self._substitute(template, **kwargs)
        return message

    @staticmethod
    def _template(messages: ConfigParser, section: str, key: str) -> str:
        """Get message string from section and key

        Args:
            messages (ConfigParser): Message file
            key (str): Key
            section (str): Section

        Returns:
            str: Message

        Raises:
            ValueError: If message section or key is not found

        """
        try:
            return messages.get(section, key)
        except NoSectionError:
            raise ValueError(Messenger.ERROR_MESSAGE_SECTION_NOT_FOUND)
        except NoOptionError:
            raise ValueError(Messenger.ERROR_MESSAGE_KEY_NOT_FOUND)
        except Exception:
            raise ValueError(Messenger.ERROR_MESSAGE_UNEXPECTED)

    @staticmethod
    def _substitute(template: str, **kwargs) -> str:
        """Substitute template with arguments

        Args:
            template (str): Template
            kwargs (dict): Arguments

        Returns:
            str: Message

        Raises:
            ValueError: If required arguments are missing
        """
        try:
            return Template(template).substitute(**kwargs)
        except KeyError:
            raise ValueError(Messenger.ERROR_MESSAGE_ARGS_MISSING)
