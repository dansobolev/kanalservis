import datetime

import requests
import xml.etree.ElementTree as ET


def get_dollar_exchange_rate() -> float:
    request = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    parser = ET.fromstring(request.text).find("./Valute[CharCode='USD']/Value").text.replace(",", ".")
    usd_rate = float(parser)
    return usd_rate


def convert_str_to_date_object(date_: str) -> datetime:
    day, month, year = date_.split('.')
    correct_format = f'{year}-{month}-{day}'
    date_obj = datetime.date.fromisoformat(correct_format)
    return date_obj
