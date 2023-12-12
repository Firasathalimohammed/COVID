import pandas as pd

class CovidDataLoader:
    """
    A class for loading COVID-19 data from a CSV file into a Pandas DataFrame.

    This class simplifies the process of reading data from CSV files, handling potential
    errors during the file reading process, and providing meaningful error messages.

    Attributes
    ----------
    file_path : str
        The file path to the CSV file containing COVID-19 data.

    Methods
    -------
    load_data():
        Reads data from the CSV file specified by the file_path attribute and returns
        it as a Pandas DataFrame.
    """

    def __init__(self, file_path):
        """
        Initializes the CovidDataLoader with the specified file path.

        Parameters
        ----------
        file_path : str
            The file path to the CSV file containing COVID-19 data to be loaded.
        """
        self.file_path = file_path

    def load_data(self):
        """
        Loads data from the CSV file into a Pandas DataFrame.

        This method attempts to read the CSV file using Pandas and handles exceptions
        by printing an error message and returning None.

        Returns
        -------
        DataFrame or None
            The loaded data as a Pandas DataFrame if successful, or None if an error occurs.
        """
        try:
            df = pd.read_csv(self.file_path)
            return df
        except Exception as e:
            print(f"An error occurred while loading the data: {e}")
            return None
