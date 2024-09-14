# nglcobdai-utils

This is a utility library for Python.

|                 |                                                                                                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **License**     | ![LICENSE](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)                                                                                                 |
| **Environment** | ![Python](https://img.shields.io/badge/-Python_3.10-F9DC3E.svg?logo=python&style=flat) ![Poetry](https://img.shields.io/badge/-Poetry-2c2d72.svg?logo=python&style=flat) |
|                 |

## Requirements

- Poetry

## Installation

### 1. Edit `pyproject.toml` file

Add the following to your `pyproject.toml` file.

```toml
[tool.poetry.dependencies]
nglcobdai-utils = {git = "https://github.com/nglcobdai/nglcobdai_utils.git", tag = "v0.0.1"}

```

### 2. Install the package

Then run the following command.

```sh
$ poetry lock
```

## Dependencies

Required libraries are as follows.  
Refer to the [`pyproject.toml`](pyproject.toml) file for the latest version.

| Library           | Version |
| ----------------- | ------- |
| pydantic          | ^1.8.2  |
| python            | ^3.10   |
| pydantic-settings | ^2.4.0  |
| pytz              | ^2024.1 |
| pyyaml            | ^6.0.2  |
| slack-sdk         | ^3.32.0 |

## Usage

### Settings

`Settings` class is a utility class that reads the settings from the `.env` file.

#### 1. Create a `.env` file in the root directory of your project.

#### 2. Add the following settings to the `.env` file.

```.env
PROJECT_NAME=hoge
```

#### 3. Use the `Settings` class to read the settings.

```py
from nglcobdai_utils import Settings
settings = Settings()
print(settings.PROJECT_NAME)
```

### Logger

`Logger` class is a utility class that creates a logger object.  
`log_file` is optional. If you want to log to a file, you can specify the file path.

#### Use the `Logger` class to create a logger object.

```python
from nglcobdai_utils import Logger

logger = Logger(__name__, log_file='app.log').logger
logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')
```

`app.log` will be created in the root directory of your project.

### Slack

`Slack` class is a utility class that sends messages to Slack.

#### 1. Set up the Slack App

Refer to the [how to create a Slack App](/doc/how_to_setup_slack_app.md) for more information.

#### 2. Use the `Slack` class to send messages to Slack.

`token` is the Bot User OAuth Access Token that you got when you [created a Slack App](/doc/how_to_setup_slack_app.md).

```python
from nglcobdai_utils import Slack

slack = Slack(token="xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxx")
slack.post_text(channel="general", text="Hello, World!")    # Send a text message
slack.post_file(channel="general", files=[{"file": "README.md", "title": "README.md"}]) # Send a file
```
