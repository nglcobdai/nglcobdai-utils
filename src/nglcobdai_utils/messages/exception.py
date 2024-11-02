from nglcobdai_utils.base import BaseException


class MessageFileNotFoundException(BaseException):
    _CODE = "NUE0000"
    """str: Error code"""

    _MESSAGE = (
        "The message file could not be found. "
        "Please check the file path and try again."
    )
    """str: Error message displayed when the message file is missing."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MessageMissingSectionHeaderException(BaseException):
    _CODE = "NUE0001"
    """str: Error code"""

    _MESSAGE = (
        "The message file is missing a required section header. "
        "Please add the section header [XXX] to resolve this issue."
    )
    """str: Error message for missing section header in the message file."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MessageSectionNotFoundException(BaseException):
    _CODE = "NUE0002"
    """str: Error code"""

    _MESSAGE = (
        "The specified message section could not be found. "
        "Ensure the section name is correct or add the section if missing."
    )
    """str: Error message displayed when the message section is missing."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MessageKeyNotFoundException(BaseException):
    _CODE = "NUE0003"
    """str: Error code"""

    _MESSAGE = (
        "The specified message code could not be found. "
        "Verify the key name or add it to the relevant section in the file."
    )
    """str: Error message displayed when the specified message key is not found."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MessageMissingArgumentsException(BaseException):
    _CODE = "NUE0004"
    """str: Error code"""

    _MESSAGE = (
        "Some required arguments are missing from the template. "
        "Please provide all necessary arguments and try again."
    )
    """str: Error message displayed when arguments are missing in the template."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MessageUnexpectedException(BaseException):
    _CODE = "NUE0005"
    """str: Error code"""

    _MESSAGE = (
        "An unexpected error occurred while retrieving the message. "
        "Please review the file format and content for any irregularities."
    )
    """str: Error message displayed when an unexpected error occurs."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
