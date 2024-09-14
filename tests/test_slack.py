from nglcobdai_utils.slack import Slack
from nglcobdai_utils.config import Settings


class TestSlack:
    @classmethod
    def setup_class(cls):
        cls.settings = Settings()
        cls.slack = Slack(cls.settings.SLACK_BOT_TOKEN)

    def test_slack_api_test(self):
        api_response = self.slack.client.api_test()
        assert api_response["ok"]

    def test_slack(self):
        response = self.slack.post_text(
            channel=self.settings.SLACK_CHANNEL,
            text="This is a pytest message from nglcobdai-utils.",
        )
        assert response["ok"]

    def test_slack_file(self):
        response = self.slack.post_file(
            channel=self.settings.SLACK_CHANNEL,
            files=[
                {"file": "README.md", "title": "README.md"},
                {"file": "LICENSE", "title": "LICENSE"},
            ],
            initial_comment="This is a pytest file upload from nglcobdai-utils.",
        )
        assert response["ok"]
