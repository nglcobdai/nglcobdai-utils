Messenger
=========

The ``Messenger`` class is used to load and retrieve messages from a configuration file. 
It allows you to define and manage fixed messages, as well as messages with placeholders for variable substitution.

Creating a Messenger Instance
-----------------------------

To create a ``Messenger`` instance, first create a configuration file in `.ini` format to store your messages.

.. code-block:: bash

   $ touch messages.ini

Define your messages in the `.ini` file with optional placeholders for variables:

.. code-block:: ini
    
   # messages.ini
   [MESSAGES]
   message1 = Hello World!
   message2 = Hello {name}!

Using the ``Messenger`` Class
-----------------------------

The following example demonstrates how to use the ``Messenger`` class to retrieve messages with and without placeholders.

.. code-block:: python

   from nglcobdai_utils import Messenger

   messenger = Messenger("messages.ini")
   print(messenger("MESSAGES", "message1"))  # Output: Hello World!
   print(messenger("MESSAGES", "message2", name="Mike"))  # Output: Hello Mike!
