Logger
======

``Logger`` class is a utility class that creates a logger object.
``log_file`` is optional. If you want to log to a file, you can specify the file path.

Use the ``Logger`` class to create a logger object.
---------------------------------------------------

.. code-block:: python

   from nglcobdai_utils import ConsoleHandlerInfo, FileHandlerInfo, StringHandlerInfo, get_logger

   ch = ConsoleHandlerInfo(log_level="INFO")
   fh = FileHandlerInfo(log_level="DEBUG", log_file="logs/app.log")
   sh = StringHandlerInfo(log_level="INFO")
   logger = get_logger("app", ch_info=ch, fh_info=fh, sh_info=sh)
   logger.debug('This is a debug message.')
   logger.info('This is an info message.')
   logger.warning('This is a warning message.')
   logger.error('This is an error message.')

``app.log`` will be created in the root directory of your project.
