from nglcobdai_utils import Settings, Slack, StringHandlerInfo, get_logger


class TestSlack:
    @classmethod
    def setup_class(cls):
        cls.settings = Settings()
        string_handler_info = StringHandlerInfo(log_level="DEBUG")
        cls.logger = get_logger(name="test_slack_logger", sh_info=string_handler_info)
        cls.slack = Slack(cls.settings.SLACK_BOT_TOKEN)

    def test_slack_api_test(self):
        api_response = self.slack.client.api_test()
        assert api_response["ok"]

    def test_slack_post_text(self):
        self.logger.info("This is a pytest message from nglcobdai-utils.")
        response = self.slack.post_text(
            channel=self.settings.SLACK_CHANNEL,
            text=self.logger.get_log_message(),
        )
        assert response["ok"]

    def test_slack_post_file(self):
        self.logger.info("This is a pytest file upload from nglcobdai-utils.")
        response = self.slack.post_file(
            channel=self.settings.SLACK_CHANNEL,
            files=[
                {"file": "sample/file.test.txt", "title": "file.test.txt"},
            ],
            initial_comment=self.logger.get_log_message(),
        )
        assert response["ok"]
