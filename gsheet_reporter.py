import gspread
import os

from oauth2client.service_account import ServiceAccountCredentials

class GSheetReporter:

    def __init__(self, credentials_file, sheet_file_key):
        CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
        scope = ['https://spreadsheets.google.com/feeds']

        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(CURRENT_DIR, credentials_file), scope)
        self.sheet_file_key = sheet_file_key
        self.sheet = gspread.authorize(self.credentials).open_by_key(sheet_file_key)

    def insert(self, worksheet_name, data_array, idx=1):
        worksheet = self.getWorksheet(worksheet_name)
        worksheet.insert_row(values=data_array, index=idx)

    def getWorksheet(self, name):
        existing_sheets = self.sheet.worksheets()

        titles = list(map(lambda x:x.title, existing_sheets))
        if (name in titles):
            worksheet = self.sheet.worksheet(name)
        else:
            worksheet = self.sheet.add_worksheet(title=name, rows="100", cols="10")

        return(worksheet)