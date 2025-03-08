
Car Valuation Project
This project is used to automate car valuation tests by extracting data from a given input file, navigating to a car valuation website, and checking if the car details (make, model, year) match the expected results provided in an output file.

Project Overview
This repository contains the code for automating car valuation tests using Playwright and pytest. The tests verify that the car details, such as the make, model, and year, match the expected values by searching the car registration number on the car valuation website.

The project performs the following steps:

Extracts vehicle registration numbers from an input file.
Navigates to a car valuation website using Playwright.
Searches for vehicle details by the registration number.
Compares actual car details (make, model, year) with the expected values from an output file.
Handles errors if the car cannot be found.
Prerequisites
Before running the tests, make sure you have the following dependencies installed:

Python 3.x
pytest: To run the tests.
playwright: For browser automation.
Install Dependencies
Clone this repository:

git clone https://github.com/your-repository-url.git

Configuration
Input and Output Files
Input file (datafiles/car_input.txt): Contains the car registration numbers to search for and the search engine url.
Output file (datafiles/car_output.txt): Contains the expected car details (make, model, and year) for comparison.
The input file should contain car registration numbers, and the output file should contain a CSV-like format with expected details.

Example of car_output.txt format:

VARIANT_REG,MAKE,MODEL,YEAR
SG18 HTN,VOLKSWAGEN,GOLF SE NAVIGATION TSI EVO,2018
AD58 VNF,BMW,120D M SPORT,2008

Test Settings
URL Pattern: The code is designed to extract a valid car valuation URL from the input file. If no URL is found, the default URL https://car-checking.com will be used.
Car Registration Number Pattern: The code expects registration numbers in the format of UK vehicle plates (e.g., AB12 CDE).

Running the Tests
To run the tests, simply use the following command:

pytest -s tests/

This will start the test suite, which will:

Open a browser.
Navigate to the car valuation website.
Search for each vehicle registration number.
Compare the car details with the expected results.

Debugging
If you need to debug the tests, you can run Playwright in headful mode (non-headless) by modifying the browser.launch method in the browser fixture:

browser = p.chromium.launch(headless=False)
Test Results
Once the tests have completed, the results will be displayed in the terminal, showing any mismatches between the actual car details and the expected values.

Project Structure

/car-valuation
│
├── datafiles/
│   ├── car_input.txt      # Input file containing car registration numbers
│   └── car_output.txt     # Output file containing expected car details
│
├── test_car_valuation.py  # Test file with pytest test cases
├── car_valuation.py       # CarValuationPage class for interacting with the website
├── requirements.txt       # List of dependencies
└── README.md              # This file

Note:

I have updated an invalid registration number with a valid registration number and have picked two registration numbers as else motorway.co.uk is giving timeout error and also i am in progress of handling invalid registration numbers
