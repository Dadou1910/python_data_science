import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
Load a CSV file.

Args:
    path (str): Path to the CSV file.

Returns:
    pandas.DataFrame: The loaded dataset.
"""
    try:
        file = pd.read_csv(path)
    except (TypeError, ValueError, FileNotFoundError) as e:
        print(type(e), __name__, e)
        return None
    return file
