# YC Scraper

YC Scraper is a Python script that extracts information about Y Combinator companies from a local HTML file and the Y Combinator website.

## Features

- Scrapes company information from a local HTML file
- Fetches additional details from individual company pages on the Y Combinator website
- Extracts the following information for each company:
  - Company Name
  - Short Description
  - Company Website
  - Y Combinator URL
  - Industries
  - Full Description
  - Founders
  - LinkedIn Profiles
- Outputs the data to a CSV file

## Requirements

- Python 3.x
- Required Python packages:
  - requests
  - beautifulsoup4
  - pandas

## Installation

1. Clone this repository or download the `ycscraper.py` file.
2. Install the required packages:

## Usage

1. Save the Y Combinator batch page as an HTML file (e.g., `yc24.html`).
2. Run the script: `python ycscraper.py`
3. The script will generate a CSV file named `yc_batch24.csv` with the scraped data.

## Customization

- To change the input file name, modify the `file_path` variable in the `__main__` section of the script.
- To change the output file name, modify the second argument in the `write_to_csv()` function call in the `__main__` section.

## Note

This script is for educational purposes only. Make sure to comply with Y Combinator's terms of service and respect their website's robots.txt file when using this script.

## License

[MIT License](https://opensource.org/licenses/MIT)
