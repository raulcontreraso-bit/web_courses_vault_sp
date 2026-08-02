Functions and Classes
=====================

Click the button below to launch the live execution engine:

.. thebe-button::

Functions
---------

Python functions are defined by the ``def`` keyword. They take a number of arguments and return values.

.. code-block:: python

    def hello(name):
        """Say hello to the person given by the argument"""
        print('Hello', name)
        return 'Hello ' + name

    hello("Anne")