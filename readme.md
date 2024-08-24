# Phish Report Automation Tool

## Description

This Python script is designed to automate the process of reporting potentially malicious URLs through the [Phish.Report](https://takedown.phish.report/docs) API. It facilitates mass phishing report submissions and stores the results in JSON files within a local folder.

## Features

- **Mass Reporting**: Allows you to report up to 10 URLs at a time.
- **Takedown Automation**: Automatically initiates takedown processes for URLs identified as malicious.
- **Local Result Storage**: Saves abuse contact information and takedown responses in JSON files.

## Prerequisites

To use this script, you need the following:

- Python 3
- `requests` library installed in Python (install using `pip install requests`)
- `json` library installed in Python (install using `pip install json`)
- A valid Phish.Report API key

## Setup

1. Clone this repository or download the files to your local machine.
2. Open the script in your favorite IDE or text editor and replace `'your_real_api_key_here'` with your actual API key.
3. Ensure that the `requests` and `json` libraries are installed.

## Usage

To run the script, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script with `python repph.py`.
4. Follow the on-screen instructions to input the URLs you want to report.
5. Check the "results" folder to view the JSON files containing the report details.

## `.gitignore` Configuration

A `.gitignore` file has been configured to exclude the 'results' folder and its contents from the repository.

## Warning

Use this script with caution and ensure that only URLs you have verified as malicious are reported.

## Support

If you encounter any issues or have suggestions, please open an issue in this repository.
