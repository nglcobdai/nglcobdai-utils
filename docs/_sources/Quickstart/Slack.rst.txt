Slack
=====

``Slack`` class is a utility class that sends messages to Slack.

1. **Set up the Slack App**

   Refer to the :doc:`How to setup a Slack App <../Installation/Slack>` for more information.

2. **Use the** ``Slack`` **class to send messages to Slack.**

   ``token`` is the Bot User OAuth Access Token that you got when you `created a Slack App </doc/how_to_setup_slack_app.md>`_.

   .. code-block:: python

      from nglcobdai_utils import Slack

      slack = Slack(token="xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxx")
      slack.post_text(channel="general", text="Hello, World!")    # Send a text message
      slack.post_file(channel="general", files=[{"file": "README.md", "title": "README.md"}]) # Send a file
