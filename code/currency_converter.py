import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()
API_KEY = getenv("CURRENCY_API_KEY")
BASE_URL = "https://api.getgeoapi.com/v2/currency/"

class CurrencyConverter:
    def __init__(self, base_currency, currency_to_convert_to):
        self.base_currency = base_currency
        self.currency_to_convert_to = currency_to_convert_to

    @classmethod
    def get_supported_currency(cls):
        url = BASE_URL + "list"
        params = {
            "api_key": API_KEY,
            "format": "json"
        }
        response = requests.get(url, params=params)
        return response.json()

    def check_currency_supportivity(self):
        data = self.get_supported_currency()
        return True if self.currency_code in data['currencies'] else False

    def currency_conversion(self, amount=1, format="json"):
        url = BASE_URL + "convert"
        params = {
            "api_key": API_KEY,
            "from": self.base_currency,
            "to": self.currency_to_convert_to,
            "amount": amount,
            "format": format
        }
        response = requests.get(url, params=params)
        if response.json()['status'] == "failed" or response.json()['status'] == "fail":
            return f"ERROR: {response.json()['error']['message']}"
        return response.json()

    def currency_conversion_historic(self, date, amount=1, format='json'):
        # date must be entered in a YYYY-MM-DD format
        url = f"{BASE_URL}historical/{date}"
        params = {
            "api_key": API_KEY,
            "from": self.base_currency,
            "to": self.currency_to_convert_to,
            "amount": amount,
            "format": format
        }
        response = requests.get(url, params=params)
        if response.json()['status'] == "failed" or response.json()['status'] == "fail":
            return f"ERROR: {response.json()['error']['message']}"
        return response.json()
