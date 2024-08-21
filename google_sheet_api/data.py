import os
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.gdch_credentials import ServiceAccountCredentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SAMPLE_SPREADSHEET_ID = '1S66YBMm4nv1DlbzlJ2IFK9zO6rTanxlZG41MxnBYfw0'
SAMPLE_RANGE_NAME = "Лист1!A8:M41"


def get_data_from_sheet():
    credentials = service_account.Credentials.from_service_account_file(
        'bmd-creds-63195.json', scopes=SCOPES)

    try:
        service = build("sheets", "v4", credentials=credentials)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values")

        if not values:
            print("No data found.")
        else:
            return values

    except HttpError as err:
        print(err)


def process_data(data: list):
    keys = data.pop(0)
    return [{keys[i]: item[i] for i in range(len(keys))} for i, item in enumerate(data) if i != len(data) - 1]

