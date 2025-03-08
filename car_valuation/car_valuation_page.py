import re
from pathlib import Path

# File paths
INPUT_FILE = "car_input.txt"
OUTPUT_FILE = "car_output.txt"

class CarValuationPage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def search_vehicle(self, regno):
        regno = str(regno).replace("'", "")
        self.page.fill("#vrm-input", str(regno))
        self.page.click('[data-cy="valueButton"]')
        # self.page.wait_for_selector(self.car_details_section)

    def get_car_details(self):
        return {
            "reg_number": "reg_number",
            "make": self.page.inner_text('[data-cy="vehicleMakeAndModel"]').split()[0],
            "model": self.page.inner_text('[data-cy="vehicleMakeAndModel"]'),
            "year": self.page.inner_text('//ul[@data-cy="vehicleSpecifics"]/li[1]')
        }


