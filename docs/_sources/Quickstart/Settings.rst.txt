Settings
========

``Settings`` class is a utility class that reads the settings from the ``.env`` file.

1. **Create a** ``.env`` **file in the root directory of your project.**

2. **Add the following settings to the** ``.env`` **file.**

   .. code-block:: ini

      PROJECT_NAME=hoge

3. **Use the** ``Settings`` **class to read the settings.**

   .. code-block:: python

      from nglcobdai_utils import Settings
      settings = Settings()
      print(settings.PROJECT_NAME)
