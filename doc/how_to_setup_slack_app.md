# How to setup a Slack App

## Prerequisites

- [Slack Workspace](https://slack.com/)

## Steps

### 1. Create a Slack App

- 1-1. Access the [slack api](https://api.slack.com/apps)

- 1-2. Click the `Create New App` button.

- 1-3. Select the `From scratch` option.

- 1-4. Enter the `App Name` and select the `${Development Slack Workspace}`.

- 1-5. Click the `Create App` button.

### 2. Set up the Slack App

- 2-1. Click the `OAuth & Permissions` menu in the `Features` section.

- 2-2. Click the `Add an OAuth Scope` button in `Bot Token Scopes` of the `Scopes` section and add the following scopes.

  | Scope                  | Description                                                                                   |
  | ---------------------- | --------------------------------------------------------------------------------------------- |
  | `channels:read`        | View basic information about public channels in a workspace                                   |
  | `chat:write`           | Send messages as @nglcobdai-utils-Bot                                                         |
  | `chat:write.customize` | Send messages as @nglcobdai-utils-Bot with a customized username and avatar                   |
  | `chat:write.public`    | Send messages to channels @nglcobdai-utils-Bot isn't a member of                              |
  | `files:write`          | Upload, edit, and delete files as nglcobdai-utils-Bot                                         |
  | `groups:read`          | View basic information about private channels that nglcobdai-utils-Bot has been added to      |
  | `im:read`              | View basic information about direct messages that nglcobdai-utils-Bot has been added to       |
  | `mpim:read`            | View basic information about group direct messages that nglcobdai-utils-Bot has been added to |
  |                        |                                                                                               |

### 3. Install the Slack App to the Workspace

- 3-1. Click the `Install App` section in the `Settings` menu.

- 3-2. Click the `Install to Workspace` button.

- 3-3. Click the `Allow` button.

### 4. Get the Bot User OAuth Access Token

- 4-1. Click the `OAuth & Permissions` menu in the `Features` section.

- 4-2. Copy the `Bot User OAuth Access Token`.
