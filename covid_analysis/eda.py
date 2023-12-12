import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class COVID_EDA:
    """
    A class for conducting exploratory data analysis on COVID-19 data.

    This class provides methods for visualizing trends, patterns, and correlations
    within COVID-19 data, such as case counts, death rates, and vaccination progress.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        A DataFrame containing COVID-19 data.

    Methods
    -------
    show_basic_info()
        Prints the information about the DataFrame.
    plot_case_trends(country_code)
        Plots daily cases and deaths for a specified country.
    compare_countries(countries)
        Compares total cases and deaths among a list of countries.
    # ... (other methods)
    """

    def __init__(self, dataframe):
        """
        Initialize the class with a DataFrame.

        Parameters
        ----------
        dataframe : pandas.DataFrame
            A DataFrame containing COVID-19 data.
        """
        self.df = dataframe

    def show_basic_info(self):
        """
        Prints basic information about the DataFrame.
        """
        print(self.df.info())

    def plot_case_trends(self, country_code):
        """
        Plots daily cases and deaths for a specific country.
        :param country_code: ISO code of the country (e.g., 'USA').
        """
        country_data = self.df[self.df['iso_code'] == country_code]
        plt.figure(figsize=(12, 6))
        plt.plot(country_data['date'], country_data['new_cases'], label='Daily Cases')
        plt.plot(country_data['date'], country_data['new_deaths'], label='Daily Deaths')
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.title(f'COVID-19 Daily Cases and Deaths Trend in {country_code}')
        plt.legend()
        plt.show()

    def compare_countries(self, countries):
        """
        Compares total cases and deaths among given countries.
        :param countries: List of ISO country codes.
        """
        comparison_df = self.df[self.df['iso_code'].isin(countries)]
        comparison_df = comparison_df.groupby('iso_code').max()
        comparison_df[['total_cases', 'total_deaths']].plot(kind='bar')
        plt.title('Comparison of Total Cases and Deaths')
        plt.ylabel('Count')
        plt.show()

    def plot_vaccinations(self, country_code):
        """
        Plots vaccination data for a specific country.
        :param country_code: ISO code of the country.
        """
        country_data = self.df[self.df['iso_code'] == country_code]
        plt.figure(figsize=(12, 6))
        plt.plot(country_data['date'], country_data['people_vaccinated'], label='People Vaccinated')
        plt.plot(country_data['date'], country_data['people_fully_vaccinated'], label='People Fully Vaccinated')
        plt.xlabel('Date')
        plt.ylabel('Number of People')
        plt.title(f'Vaccination Progress in {country_code}')
        plt.legend()
        plt.show()

    def show_correlation_matrix(self):
        """
        Displays the correlation matrix of the DataFrame.
        """
        plt.figure(figsize=(10, 10))
        sns.heatmap(self.df.corr(), annot=True, fmt='.2f', cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.show()

    def plot_new_cases_over_time(self, continent=None):
        """
        Plots new cases over time. Can be filtered by continent.
        :param continent: (optional) name of the continent to filter the data.
        """
        if continent:
            data = self.df[self.df['continent'] == continent]
        else:
            data = self.df
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=data, x='date', y='new_cases', hue='continent')
        plt.title('New COVID-19 Cases Over Time' + ('' if not continent else f' in {continent}'))
        plt.xlabel('Date')
        plt.ylabel('New Cases')
        plt.show()

    def plot_death_case_ratio(self):
        """
        Plots the ratio of deaths to cases for each country.
        """
        ratio_df = self.df.groupby('location').apply(lambda x: x['total_deaths'].max() / x['total_cases'].max())
        ratio_df = ratio_df.reset_index()
        ratio_df.columns = ['location', 'death_case_ratio']
        plt.figure(figsize=(12, 6))
        sns.barplot(data=ratio_df.sort_values('death_case_ratio', ascending=False).head(20), x='death_case_ratio', y='location')
        plt.title('Top 20 Countries by Death to Case Ratio')
        plt.xlabel('Death to Case Ratio')
        plt.ylabel('Country')
        plt.show()

    def distribution_of_cases(self):
        """
        Shows the distribution of total cases globally.
        """
        plt.figure(figsize=(12, 6))
        sns.histplot(self.df['total_cases'], kde=True)
        plt.title('Global Distribution of Total COVID-19 Cases')
        plt.xlabel('Total Cases')
        plt.ylabel('Frequency')
        plt.show()

    def boxplot_cases_by_continent(self):
        """
        Displays a boxplot of cases by continent.
        """
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=self.df, x='continent', y='total_cases')
        plt.title('Boxplot of COVID-19 Cases by Continent')
        plt.xlabel('Continent')
        plt.ylabel('Total Cases')
        plt.show()

    def scatterplot_tests_vs_cases(self):
        """
        Scatter plot of total tests vs total cases.
        """
        plt.figure(figsize=(12, 6))
        sns.scatterplot(data=self.df, x='total_tests', y='total_cases', hue='continent', size='population', sizes=(20, 200))
        plt.title('Total Tests vs Total Cases by Continent')
        plt.xlabel('Total Tests')
        plt.ylabel('Total Cases')
        plt.show()

    def plot_vaccination_progress(self, country):
        """
        Plots the vaccination progress for a specific country.
        :param country: name of the country.
        """
        country_data = self.df[self.df['location'] == country]
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=country_data, x='date', y='total_vaccinations')
        plt.title(f'Vaccination Progress in {country}')
        plt.xlabel('Date')
        plt.ylabel('Total Vaccinations')
        plt.show()

    def compare_cases_continents(self):
        """
        Compares total cases across continents.
        """
        continent_data = self.df.groupby('continent')['total_cases'].max().reset_index()
        plt.figure(figsize=(12, 6))
        sns.barplot(data=continent_data, x='continent', y='total_cases')
        plt.title('Total COVID-19 Cases by Continent')
        plt.xlabel('Continent')
        plt.ylabel('Total Cases')
        plt.show()

    def plot_daily_deaths(self, country_code):
        """
        Plots daily deaths for a specific country identified by its ISO code.
        :param country_code: ISO code of the country.
        """
        country_data = self.df[self.df['iso_code'] == country_code]
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=country_data, x='date', y='new_deaths')
        plt.title(f'Daily COVID-19 Deaths in {country_code}')
        plt.xlabel('Date')
        plt.ylabel('New Deaths')
        plt.show()

    def heatmap_of_correlations(self):
        """
        Displays a heatmap of correlations between different numerical features.
        """
        plt.figure(figsize=(12, 10))
        sns.heatmap(self.df.corr(), annot=True, cmap='coolwarm')
        plt.title('Heatmap of Feature Correlations')
        plt.show()

    def plot_population_vs_cases(self):
        """
        Scatter plot comparing population with total cases.
        """
        plt.figure(figsize=(12, 6))
        sns.scatterplot(data=self.df, x='population', y='total_cases', hue='continent')
        plt.title('Population vs Total COVID-19 Cases by Continent')
        plt.xlabel('Population')
        plt.ylabel('Total Cases')
        plt.show()


