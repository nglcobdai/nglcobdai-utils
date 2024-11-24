from nglcobdai_utils import log as logging


class TemplateError(Exception):
    """
    Custom exception that formats error messages with a code and note.
    Allows customization of the message format, code, and note.
    """

    _MESSAGE_FORMAT = "{code}: {note}"
    """str: Default message format."""

    _CODE = "NGL-TPL-E9999"
    """str: Default error code"""

    _NOTE = "An unexpected error occurred."
    """str: Default note message."""

    def __init__(self, **kwargs):
        """
        Initialize with optional keyword arguments for note formatting.

        Args:
            **kwargs: Formatting arguments for the note.
        """
        self.kwargs = kwargs

        if logging.logger is not None:
            logging.logger.error(self.message)

    def __str__(self):
        """
        Return the formatted error message with code and note.

        Returns:
            str: Formatted error message.
        """
        return self.message_format.format(
            code=self.code,
            note=self.note.format(**self.kwargs),
        )

    @property
    def message(self):
        """Full error message as a string.

        Returns:
            str: Formatted error message.
        """
        return self.__str__()

    @property
    def message_format(self):
        """Current message format.

        Returns:
            str: Message format.
        """
        return self._MESSAGE_FORMAT

    @classmethod
    def set_message_format(cls, value):
        """
        Set a new format for the error message.

        Args:
            value (str): New message format.
        """
        cls._MESSAGE_FORMAT = value

    @property
    def code(self):
        """Error code.

        Returns:
            str: Error code.
        """
        return self._CODE

    @classmethod
    def set_code(cls, value):
        """
        Set a new error code.

        Args:
            value (str): New error code.
        """
        cls._CODE = value

    @property
    def note(self):
        """Note message with optional placeholders.

        Returns:
            str: Note message.
        """
        return self._NOTE

    @classmethod
    def set_note(cls, value):
        """
        Set a new note message.

        Args:
            value (str): New note message.
        """
        cls._NOTE = value
