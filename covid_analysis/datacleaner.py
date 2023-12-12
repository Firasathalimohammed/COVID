import pandas as pd

class COVIDDataCleaner:
    """
    A class used to clean COVID-19 data within a Pandas DataFrame.

    This class provides a variety of methods to preprocess the data by handling missing values,
    dropping unnecessary columns, resetting the index, removing duplicates, filtering, sorting,
    and converting column data types.

    Attributes:
    -----------
    df : DataFrame
        A Pandas DataFrame containing COVID-19 data to be cleaned.

    Methods:
    --------
    convert_date_column():
        Converts the 'date' column to a datetime format.
        
    fill_missing_values(columns, fill_value=0):
        Fills missing values in specified columns with a provided value.
        
    drop_unnecessary_columns(columns):
        Drops columns that are not required for analysis.
        
    remove_rows_with_missing_values():
        Removes rows that have all values missing.
        
    reset_index():
        Resets the index of the DataFrame after cleaning operations.
        
    remove_duplicate_rows():
        Removes duplicate rows in the DataFrame.
        
    replace_values(column, old_value, new_value):
        Replaces specific values in a column with new values.
        
    filter_by_value(column, value):
        Filters the DataFrame based on a value in a specific column.
        
    sort_data(column, ascending=True):
        Sorts the DataFrame by a specific column.
        
    drop_rows_with_missing_values_in_column(column):
        Drops rows where the specified column has missing values.
        
    convert_column_type(column, dtype):
        Converts the data type of a column to a specified new data type.
        
    get_cleaned_data():
        Returns the cleaned DataFrame.
    """

    def __init__(self, dataframe):
        """
        Constructs all the necessary attributes for the COVIDDataCleaner object.

        Parameters:
        -----------
        dataframe : DataFrame
            A Pandas DataFrame with COVID-19 data to be cleaned.
        """
        self.df = dataframe

    def convert_date_column(self):
        """ Converts the 'date' column to datetime format. """
        self.df['date'] = pd.to_datetime(self.df['date'])

    def fill_missing_values(self, columns, fill_value=0):
        """
        Fills missing values in specified columns with a given value (default is 0).
        :param columns: list of columns to fill missing values in.
        :param fill_value: value to fill missing values with.
        """
        for column in columns:
            if column in self.df.columns:
                self.df[column].fillna(fill_value, inplace=True)

    def drop_unnecessary_columns(self, columns):
        """
        Drops unnecessary columns from the DataFrame.
        :param columns: List of column names to drop.
        """
        self.df.drop(columns=columns, inplace=True, errors='ignore')

    def remove_rows_with_missing_values(self):
        """ Removes rows where all values are missing. """
        self.df.dropna(how='all', inplace=True)

    def reset_index(self):
        """ Resets the DataFrame index. """
        self.df.reset_index(drop=True, inplace=True)

    def remove_duplicate_rows(self):
        """ Removes duplicate rows. """
        self.df.drop_duplicates(inplace=True)

    def replace_values(self, column, old_value, new_value):
        """
        Replaces specific values in a column.
        :param column: Column name.
        :param old_value: Value to replace.
        :param new_value: New value.
        """
        self.df[column] = self.df[column].replace(old_value, new_value)

    def filter_by_value(self, column, value):
        """
        Filters the DataFrame based on a value in a specific column.
        :param column: Column name.
        :param value: Value to filter by.
        """
        return self.df[self.df[column] == value]

    def sort_data(self, column, ascending=True):
        """
        Sorts the DataFrame based on a specific column.
        :param column: Column name to sort by.
        :param ascending: Boolean, True for ascending sort, False for descending.
        """
        self.df.sort_values(by=column, ascending=ascending, inplace=True)

    def drop_rows_with_missing_values_in_column(self, column):
        """
        Drops rows where a specific column has missing values.
        :param column: Column name.
        """
        self.df.dropna(subset=[column], inplace=True)

    def convert_column_type(self, column, dtype):
        """
        Converts the data type of a specific column.
        :param column: Column name.
        :param dtype: New data type.
        """
        self.df[column] = self.df[column].astype(dtype)

    def get_cleaned_data(self):
        """ Returns the cleaned DataFrame. """
        return self.df


