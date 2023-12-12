### `README.md`

```markdown
# COVID-19 Data Analysis

## Overview
This Python package is designed for the analysis of COVID-19 data. It provides tools for scraping, downloading, loading, cleaning, and visualizing COVID-19 case and vaccination data.

## Features
- Scrape up-to-date COVID-19 data from Worldometer.
- Download datasets from trusted sources like Our World in Data.
- Load, clean, and preprocess data for analysis.
- Visualize case trends, death rates, and vaccination progress.
- Perform statistical analysis to understand correlations and patterns.

## Installation
Clone the repository and navigate to the project directory. Then install the package using:

```bash
pip install .
```

## Usage
The package provides several classes for different aspects of data analysis. Here's a quick start:

```python
from covid_analysis.scrape import CovidDataScraper
from covid_analysis.scrape import CovidDataDownloader
from covid_analysis.dataloader import CovidDataLoader
from covid_analysis.datacleaner import COVIDDataCleaner
from covid_analysis.eda import COVID_EDA

# Example: Load data and perform EDA
loader = CovidDataLoader('path/to/data.csv')
data = loader.load_data()
eda = COVID_EDA(data)
eda.plot_case_trends('USA')
```

## Contributing
We welcome contributions to improve this package. Please feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

In the `README.md`, you should replace `path/to/data.csv` with the actual path to the COVID-19 data CSV file. Additionally, make sure to fill in the `Your Name` and `your.email@example.com` placeholders with your actual name and email address.

To use the `setup.py`, make sure you have a `LICENSE` file in the same directory if you're mentioning it in your `README.md`. Also, adjust the `url` field to point to the actual URL of your GitHub repository.

Before running `pip install .`, ensure that your project directory has an `__init__.py` file in the package directory to be recognized as a Python package.