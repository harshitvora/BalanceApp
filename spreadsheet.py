import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

client = gspread.authorize(creds)

sheet = client.open('BalanceApp').sheet1

# retrieve

transactions = sheet.get_all_records()
print(transactions)
transactions = sheet.row_values(6)
print(transactions)
transactions = sheet.cell(6, 11).value
print(transactions)

# update

sheet.update_cell(6, 11, '555-555-5555')

#insert

row = ["This", "is", "a", "test", "update"]
index = 3
sheet.insert_row(row, index)

# delete

sheet.delete_row(3)


# meta data

rows = sheet.row_count