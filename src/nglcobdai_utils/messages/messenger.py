from configparser import (
    ConfigParser,
    MissingSectionHeaderError,
    NoOptionError,
    NoSectionError,
)
from pathlib import Path
from string import Template

from src.nglcobdai_utils.messages.error import (
    MessengerFileNotFoundError,
    MessengerKeyNotFoundError,
    MessengerMissingArgumentsError,
    MessengerMissingSectionHeaderError,
    MessengerSectionNotFoundError,
    MessengerUnexpectedError,
)


class Messenger:
    """Messenger class to retrieve messages from a message file."""

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
            MessengerFileNotFoundError: If the message file is not found.
            MessengerMissingSectionHeaderError: If the message file is missing a required section header.
        """
        if not filepath.exists():
            raise MessengerFileNotFoundError()

        try:
            config = ConfigParser()
            config.read(str(filepath), encoding="utf-8")
            return config
        except MissingSectionHeaderError:
            raise MessengerMissingSectionHeaderError()
        except Exception:
            raise MessengerUnexpectedError()

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
            MessengerSectionNotFoundError: If section is not found
            MessengerKeyNotFoundError: If key is not found
            MessengerUnexpectedError: If unexpected error occurs

        """
        try:
            return messages.get(section, key)
        except NoSectionError:
            raise MessengerSectionNotFoundError()
        except NoOptionError:
            raise MessengerKeyNotFoundError()
        except Exception:
            raise MessengerUnexpectedError()

    @staticmethod
    def _substitute(template: str, **kwargs) -> str:
        """Substitute template with arguments

        Args:
            template (str): Template
            kwargs (dict): Arguments

        Returns:
            str: Message

        Raises:
            MessengerMissingArgumentsError: If required arguments are missing
        """
        try:
            return Template(template).substitute(**kwargs)
        except KeyError:
            raise MessengerMissingArgumentsError()
        except Exception:
            raise MessengerUnexpectedError()
