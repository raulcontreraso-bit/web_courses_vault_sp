Pandas Data Wrangling
=====================

Click the button below to launch the live interactive Python kernel:

.. thebe-button::

Let's start by importing Pandas and loading data:

.. code-block:: python

    import pandas as pd
    url = "https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv"
    df = pd.read_csv(url)
    df.head()