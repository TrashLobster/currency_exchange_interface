from datetime import date, datetime
from dotenv import load_dotenv
from os import getenv
from currency_converter import CurrencyConverter as converter


# base_currency = "NZD"
# currency_convert_to = "JPY"
currency_list = [k + " - " + v for (k,v) in converter.get_supported_currency()["currencies"].items()]
print(currency_list)
# converter = CurrencyConverter(api_key, base_currency, currency_convert_to)

# get data from today
today = date.isoformat(datetime.today())
