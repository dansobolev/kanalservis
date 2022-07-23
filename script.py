import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

from utils import get_dollar_exchange_rate
from db.query import update_entities_state

CREDENTIALS_FILE = 'credentials.json'
SPREADSHEET_TABLE_ID = '1qqrEwDercKCBlX6XcZRPA7Tn-OBsfMUh0SOllBQUGdI'


def get_google_service():
    creds_json = CREDENTIALS_FILE
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return apiclient.discovery.build('sheets', 'v4', http=creds_service)


def run_parser_forever():
    while True:
        service = get_google_service()
        resp = service.spreadsheets().values()\
            .get(spreadsheetId=SPREADSHEET_TABLE_ID, range="Лист1!A1:D999").execute()

        usd_rate = get_dollar_exchange_rate()

        data = resp['values'][1:]
        for i in range(len(data)):
            price_dollar = int(data[i][2])
            price_rub = usd_rate * price_dollar
            data[i].append(price_rub)

        update_entities_state(data)


if __name__ == '__main__':
    run_parser_forever()
