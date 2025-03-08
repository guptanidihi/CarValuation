import pytest
import sys
import os
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from playwright.sync_api import sync_playwright
from car_valuation import CarValuationPage

input_file_path = "datafiles/car_input.txt"
output_file_path = "datafiles/car_output.txt"

def get_car_valuation_url():
    url_pattern = r"https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(?:\.[a-zA-Z]{2,6})?(?:/[a-zA-Z0-9\-._~:/?#[\]@!$&'()*+,;=]*)?|[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(?:\.[a-zA-Z]{2,6})?"

    with open(input_file_path, "r") as file:
        content = file.read()
        match = re.search(url_pattern, content)
        if match:
          url=  match.group(0)
        if not url.startswith("http://") and not url.startswith("https://"):
                url = "https://" + url
                return url
        else: 
            return "https://car-checking.com"  # Default URL if not found
        
# Function to extract vehicle registration numbers
def extract_registration_numbers():
    pattern = r"[A-Z]{2}[0-9]{2}\s?[A-Z]{3}"  # Example UK registration format
    with open(input_file_path, "r") as file:
        content = file.read()
    reg_numbers = re.findall(pattern, content)
    return reg_numbers[:2] 

# # Function to read expected results from output file
def read_expected_results():
    expected_results = {}
    with open(output_file_path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4:
                variant_reg, make, model, year = [part.strip().lower() for part in parts]
                expected_results[variant_reg] = {"make": make, "model": model, "year": year}
    return expected_results

@pytest.fixture(scope="module")
def browser():
     with sync_playwright() as p:
        browser =  p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="module")
def context(browser):
    return browser.new_context()

@pytest.fixture(scope="module")
def page(context):
    return context.new_page()



def get_test_data(file_pair):
    input_file, output_file = file_pair
    car_valuation_url = get_car_valuation_url()
    expected_results = read_expected_results()
    reg_numbers = extract_registration_numbers()
    return car_valuation_url, expected_results, reg_numbers

# Parameterized test for file pairs
@pytest.mark.parametrize("file_pair", [
    (input_file_path, output_file_path)  # Add more file pairs if needed
])
def test_car_valuation_match(page, file_pair):
    car_valuation_url, expected_results, reg_numbers = get_test_data(file_pair)
    
    for reg_number in reg_numbers:
        valuation_page = CarValuationPage(page)
        valuation_page.navigate(car_valuation_url)
        valuation_page.search_vehicle(reg_number)
        car_details = valuation_page.get_car_details()
        car_valuation_url = get_car_valuation_url()
        reg_numbers = extract_registration_numbers()
        expected_results = read_expected_results()
        assert reg_number.lower() in expected_results, f"No expected data for {reg_number}"
        expected_data = expected_results[reg_number.lower()]
        assert car_details["make"] == expected_data["make"], f"Mismatch in make for {reg_number}"
        assert car_details["model"] == expected_data["model"], f"Mismatch in model for {reg_number}"
        assert car_details["year"] == expected_data["year"], f"Mismatch in year for {reg_number}"

