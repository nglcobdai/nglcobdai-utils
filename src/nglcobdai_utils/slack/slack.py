from slack_sdk import WebClient


class Slack:
    """
    A class to interact with Slack API for sending messages and uploading files.

    Attributes:
        client (WebClient): The Slack WebClient instance to interact with Slack API.
        channels (list): A list of channels retrieved from Slack.
    """

    def __init__(self, token: str):
        """
        Initialize the Slack class with an API token.

        Args:
            token (str): The Slack API token.
        """
        self.client = WebClient(token)
        self.channels = self.get_channels()

    def get_channels(self, exclude_archived=True, **kwargs):
        """
        Retrieve the list of channels from Slack.

        Args:
            exclude_archived (bool): Whether to exclude archived channels (default: True).
            **kwargs: Additional keyword arguments passed to the Slack API.

        Returns:
            list: A list of channels.
        """
        channels = self.client.conversations_list(
            exclude_archived=exclude_archived, **kwargs
        )
        return channels["channels"]

    def get_channel_id(self, channel: str):
        """
        Retrieve the ID of a specific Slack channel by its name.

        Args:
            channel (str): The name of the Slack channel.

        Returns:
            str: The ID of the Slack channel if found, otherwise None.
        """
        channel_id = None
        for ch in self.channels:
            if ch["name"] == channel:
                channel_id = ch["id"]
                break
        return channel_id

    def post_text(self, channel: str, text: str, **kwargs):
        """
        Post a text message to a Slack channel.

        Args:
            channel (str): The name of the Slack channel.
            text (str): The message to be posted.
            **kwargs: Additional keyword arguments passed to the Slack API.

        Returns:
            dict: The Slack API response.
        """
        response = self.client.chat_postMessage(
            channel=self.get_channel_id(channel),
            text=self._validate_text(text),
            **kwargs
        )
        return response

    def post_file(self, channel: str, files: list, **kwargs):
        """
        Upload a file to a Slack channel.

        Args:
            channel (str): The name of the Slack channel.
            files (List[Dict]): A list of dictionaries containing file information.
            **kwargs: Additional keyword arguments passed to the Slack API.

        Example:
            >>> slack.post_file("general", [{"file": "README.md", "title": "README"}])

        Returns:
            dict: The Slack API response.
        """
        response = self.client.files_upload_v2(
            channel=self.get_channel_id(channel), file_uploads=files, **kwargs
        )
        return response

    def _validate_text(self, text: str):
        """
        Validate the text message before sending to Slack.

        Args:
            text (str): The text message to validate.

        Returns:
            str: The original text if valid, or a truncated version if it exceeds the limit.
                 Returns a single space if the text is empty.
        """
        if not text:
            return " "
        if len(text) == 0:
            return " "
        if len(text) > 3000:
            return text[:3000]
        return text
