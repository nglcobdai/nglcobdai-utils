from nglcobdai_utils.base import TemplateError


class MessengerFileNotFoundError(TemplateError):
    """Raised when the message file is not found."""

    _CODE = "NGU-MES-E0001"
    """str: Error code"""

    _NOTE = (
        "The message file could not be found. "
        "Please check the file path and try again."
    )
    """str: Error message displayed when the message file is missing."""


class MessengerMissingSectionHeaderError(TemplateError):
    """Raised when a required section header is missing in the message file."""

    _CODE = "NGU-MES-E0002"
    """str: Error code"""

    _NOTE = (
        "The message file is missing a required section header. "
        "Please add the section header [XXX] to resolve this issue."
    )
    """str: Error message for missing section header in the message file."""


class MessengerSectionNotFoundError(TemplateError):
    """Raised when a specified message section cannot be found in the file."""

    _CODE = "NGU-MES-E0003"
    """str: Error code"""

    _NOTE = (
        "The specified message section could not be found. "
        "Ensure the section name is correct or add the section if missing."
    )
    """str: Error message displayed when the message section is missing."""


class MessengerKeyNotFoundError(TemplateError):
    """Raised when the specified message key is not found in the section."""

    _CODE = "NGU-MES-E0004"
    """str: Error code"""

    _NOTE = (
        "The specified message code could not be found. "
        "Verify the key name or add it to the relevant section in the file."
    )
    """str: Error message displayed when the specified message key is not found."""


class MessengerMissingArgumentsError(TemplateError):
    """Raised when required arguments for the message template are missing."""

    _CODE = "NGU-MES-E0005"
    """str: Error code"""

    _NOTE = (
        "Some required arguments are missing from the template. "
        "Please provide all necessary arguments and try again."
    )
    """str: Error message displayed when arguments are missing in the template."""


class MessengerUnexpectedError(TemplateError):
    """Raised for unexpected errors while retrieving messages."""

    _CODE = "NGU-MES-E0006"
    """str: Error code"""

    _NOTE = (
        "An unexpected error occurred while retrieving the message. "
        "Please review the file format and content for any irregularities."
    )
    """str: Error message displayed when an unexpected error occurs."""
