# Amazon Product Scraper

This is a Python script that scrapes product information from Amazon and saves it into a CSV file. It utilizes `Selenium` and `webdriver-manager` to automate the browser and gather data about products, including their name, price, rating, and seller.

## Features

- Scrapes product information from an Amazon category page.
- Collects product name, price, rating, and seller name.
- Supports pagination to scrape data from multiple pages.
- Saves data to a CSV file for easy analysis.
- Runs in headless mode for efficiency (does not open a browser window).

## Requirements

Before running the script, ensure you have the following libraries installed:

- `selenium` - For web scraping and browser automation.
- `webdriver-manager` - To automatically download the correct web driver.
- `random` and `time` - For controlling delays and simulating human-like browsing behavior.

You can install the required libraries using `pip`:

```bash
pip install selenium webdriver-manager
