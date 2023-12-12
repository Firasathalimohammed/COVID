import requests
import pandas as pd
from bs4 import BeautifulSoup

class CovidDataScraper:
    """
    A class for scraping COVID-19 data from the Worldometer website.

    This class uses the requests library to fetch data from the Worldometer's COVID-19
    page and BeautifulSoup for parsing the HTML content to extract relevant data.

    Attributes
    ----------
    url : str
        The URL of the Worldometer's COVID-19 page.
    field_list : list of str
        The list of fields to extract from the data table on the Worldometer page.

    Methods
    -------
    fetch_data()
        Fetches the COVID-19 data for all countries from the Worldometer page.
    get_global_stats()
        Retrieves global COVID-19 statistics such as total cases, deaths, and recovered.
    """

    def __init__(self):
        self.url = "https://www.worldometers.info/coronavirus/"
        self.field_list = ["Name", "Total Cases", "New Cases", "Total Deaths", "New Deaths", "Total Recovered", "New Recovered", "Active Cases", "Serious Cases", "Total Tests", "Population"]

    def fetch_data(self):
        response = requests.get(self.url).text
        soup = BeautifulSoup(response, "lxml")
        world_data = soup.find("tbody").find_all("tr")[8:229]

        data = []
        for row in world_data:
            cols = [td.text.strip() for td in row.find_all("td")]
            data.append(cols[1:10] + [cols[12]] + [cols[14]])

        return pd.DataFrame(data, columns=self.field_list)

    def get_global_stats(self):
        response = requests.get(self.url).text
        soup = BeautifulSoup(response, "lxml")
        global_count = soup.find_all("div", class_="maincounter-number")

        return {
            "Total Cases": global_count[0].text.strip(),
            "Total Deaths": global_count[1].text.strip(),
            "Total Recovered": global_count[2].text.strip()
        }


class CovidDataDownloader:
    """
    A class for downloading COVID-19 data files from a specified URL.

    This class uses the requests library to perform HTTP requests for downloading data files.

    Parameters
    ----------
    url : str
        The URL from which to download the COVID-19 data file.

    Methods
    -------
    download_covid_data(output_filename=None)
        Downloads the COVID-19 data file from the specified URL.
    """

    def __init__(self, url):
        """
        Initializes the CovidDataDownloader with the specified URL.

        Parameters
        ----------
        url : str
            The URL from which to download the COVID-19 data file.
        """
        self.url = url

    def download_covid_data(self, output_filename=None):
        """
        Downloads the COVID-19 data file from the specified URL.
        If output_filename is not provided, the name is derived from the URL.
        """
        response = requests.get(self.url)

        if response.status_code == 200:
            if not output_filename:
                output_filename = self.url.split('/')[-1]

            with open(output_filename, 'wb') as file:
                file.write(response.content)

            print(f"COVID-19 data file downloaded: {output_filename}")
            return True
        else:
            print(f"Error downloading COVID-19 data. Status code: {response.status_code}")
            return False



