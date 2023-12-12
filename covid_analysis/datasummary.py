import pandas as pd

class DataSummary:
    """
    A class that provides methods for generating summaries and extracting information
    from a DataFrame containing COVID-19 data.

    Attributes
    ----------
    df : DataFrame
        A Pandas DataFrame with COVID-19 data.

    Methods
    -------
    get_basic_info():
        Returns the shape, column names, and data types of the DataFrame.
    get_missing_values_info():
        Identifies and returns a Series with counts of missing values per column.
    get_statistical_summary():
        Provides a statistical summary for numerical columns in the DataFrame.
    get_unique_values_info(column_names):
        Calculates and returns the number of unique values for the specified columns.
    print_unique_values(column_name):
        Prints the unique values found in a specified column.
    get_shape():
        Returns the shape of the DataFrame.
    get_column_names():
        Lists the column names of the DataFrame.
    get_location_value_counts():
        Counts and returns the number of unique occurrences in the 'location' column.
    check_null_values():
        Checks and returns a boolean indicating if any column contains null values.
    get_missing_values():
        Returns the total number of missing values in each column of the DataFrame.
    basic_info():
        Generates a formatted string with basic information about the DataFrame.
    country_specific_summary(country_code):
        Creates a summary of total cases, deaths, and vaccinations for a specific country.
    date_range():
        Determines the minimum and maximum dates present in the DataFrame.
    global_summary():
        Aggregates and returns global totals for cases, deaths, and vaccinations.
    continent_summary(continent):
        Provides a summary of total cases, deaths, and vaccinations for a specified continent.
    highest_case_countries(top_n):
        Identifies the top countries with the highest case counts.
    highest_death_countries(top_n):
        Identifies the top countries with the highest death counts.
    highest_vaccination_countries(top_n):
        Identifies the top countries with the highest vaccination numbers.
    trend_over_time(country_code, measure):
        Returns a time series of a specified measure for a given country.
    """
    def __init__(self, df):
        """
        Constructs all the necessary attributes for the DataSummary object.

        Parameters
        ----------
        df : DataFrame
            A Pandas DataFrame with COVID-19 data.
        """
        self.df = df

    def get_basic_info(self):
        """Returns basic information about the dataset such as shape, column names and data types."""
        info = {
            'Number of Rows': self.df.shape[0],
            'Number of Columns': self.df.shape[1],
            'Column Names': self.df.columns.tolist(),
            'Data Types': self.df.dtypes.to_dict()
        }
        return info

    def get_missing_values_info(self):
        """Returns information about missing values in the dataset."""
        missing_values = self.df.isnull().sum()
        return missing_values[missing_values > 0]

    def get_statistical_summary(self):
        """Returns a statistical summary for numerical columns in the dataset."""
        return self.df.describe()

    def get_unique_values_info(self, column_names):
        """Returns the number of unique values for specified columns."""
        unique_values = {col: self.df[col].nunique() for col in column_names}
        return unique_values

    def print_unique_values(self, column_name):
        """
        Prints unique values of a specified column.
        """
        if column_name in self.df.columns:
            unique_values = self.df[column_name].unique()
            print(f"Unique values in '{column_name}': {unique_values}")
        else:
            print(f"Column '{column_name}' not found in the dataset.")

    def get_shape(self):
        """ Returns the shape of the df. """
        return self.df.shape

    def get_column_names(self):
        """ Returns the column names of the df. """
        return self.df.columns.tolist()

    def get_location_value_counts(self):
        """ Returns the counts of unique values in the 'location' column. """
        return self.df['location'].value_counts()

    def check_null_values(self):
        """ Checks if any column has null values. """
        return self.df.isna().any()

    def get_missing_values(self):
        """ Returns the number of missing values in each column. """
        return self.df.isnull().sum()

    def basic_info(self):
        info = f"Dataset Basic Information:\n"
        info += f"-------------------------\n"
        info += f"Number of Rows: {self.df.shape[0]}\n"
        info += f"Number of Columns: {self.df.shape[1]}\n"
        info += f"Columns: {', '.join(self.df.columns)}\n"
        info += f"Missing Values per Column:\n"
        missing_values = self.df.isnull().sum()
        for column, count in missing_values.items():
            info += f"  - {column}: {count} missing\n"
        return info

    def country_specific_summary(self, country_code):
        country_data = self.df[self.df['iso_code'] == country_code]
        summary = {
            "Total Cases": country_data["total_cases"].max(),
            "Total Deaths": country_data["total_deaths"].max(),
            "Total Vaccinations": country_data["total_vaccinations"].max()
        }
        return summary

    def date_range(self):
        dates = pd.to_datetime(self.df['date'])
        return dates.min(), dates.max()

    def global_summary(self):
        summary = {
            "Global Total Cases": self.df["total_cases"].max(),
            "Global Total Deaths": self.df["total_deaths"].max(),
            "Global Total Vaccinations": self.df["total_vaccinations"].max()
        }
        return summary

    def continent_summary(self, continent):
        continent_data = self.df[self.df['continent'] == continent]
        summary = {
            "Total Cases in Continent": continent_data["total_cases"].max(),
            "Total Deaths in Continent": continent_data["total_deaths"].max(),
            "Total Vaccinations in Continent": continent_data["total_vaccinations"].max()
        }
        return summary

    def highest_case_countries(self, top_n=10):
        return self.df.groupby('location')['total_cases'].max().nlargest(top_n)

    def highest_death_countries(self, top_n=10):
        return self.df.groupby('location')['total_deaths'].max().nlargest(top_n)

    def highest_vaccination_countries(self, top_n=10):
        return self.df.groupby('location')['total_vaccinations'].max().nlargest(top_n)

    def trend_over_time(self, country_code, measure):
        country_data = self.df[self.df['iso_code'] == country_code]
        return country_data[['date', measure]].set_index('date')
