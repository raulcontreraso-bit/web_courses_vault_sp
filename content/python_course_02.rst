====================================
Course 2: Introduction to Python
====================================

Click the button below to start the interactive execution engine:

.. thebe-button::

Basic Variables & Control Flow
------------------------------

Try modifying and running the Python snippet below:

.. code-block:: python

    # Define variables
    message = "Hello, Python Student!"
    number = 42

    print(message)
    print("The answer is:", number)


Loop Statements
---------------

Loops allow executing code repeatedly.

For Loops
~~~~~~~~~

A ``for`` loop iterates over a given sequence:

.. code-block:: python

    for i in range(3):
        print(f"Iteration {i}")


While Loops
~~~~~~~~~~~

A ``while`` loop continues while a condition remains True:

.. code-block:: python

    count = 0
    while count < 3:
        print(f"Count: {count}")
        count += 1