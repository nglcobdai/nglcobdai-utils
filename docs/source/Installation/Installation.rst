Installation
============

Dependencies
------------

Required libraries are as follows. Refer to the ``pyproject.toml`` file for the latest versions.

+---------------------+---------+
| Library             | Version |
+=====================+=========+
| poetry              | ^1.8.4  |
+---------------------+---------+
| python              | ^3.10   |
+---------------------+---------+
| pydantic            | ^1.8.2  |
+---------------------+---------+
| pydantic-settings   | ^2.4.0  |
+---------------------+---------+
| pytz                | ^2024.1 |
+---------------------+---------+
| pyyaml              | ^6.0.2  |
+---------------------+---------+
| slack-sdk           | ^3.32.0 |
+---------------------+---------+

Setting
-------

.. toctree::
   :maxdepth: 1

   Slack

Install
-------


1. **Edit** ``pyproject.toml`` **file**

    | Add the following to your ``pyproject.toml`` file.
    | ``xxx`` is the version number you want to install (e.g., v1.0.0).

    .. code-block:: toml

        [tool.poetry.dependencies]
        nglcobdai-utils = {git = "https://github.com/nglcobdai/nglcobdai_utils.git", tag = "vxxx"}

2. **Install the package**

    Then run the following command.

    .. code-block:: sh

        $ poetry lock
