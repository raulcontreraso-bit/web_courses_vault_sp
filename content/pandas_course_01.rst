Course 2: Data Wrangling with Pandas
====================================

Click the button below to launch the live kernel:

.. thebe-button::

Analyzing Datasets with Pandas
------------------------------

Load and summarize a dataset in real time:

.. code-block:: python

    import pandas as pd

    # Load Titanic sample dataset
    url = "https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv"
    titanic = pd.read_csv(url)

    # Display basic info
    print("Dataset Shape:", titanic.shape)
    titanic.head()