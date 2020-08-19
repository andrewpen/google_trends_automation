print("success 1")
import pygsheets
import pandas as pd 
# authorization
gc = pygsheets.authorize(service_file='key/creds.json')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['John', 'Steve', 'Sarah']

print(df['name'])

# open the google spreadsheet (where test_sheet is the name of my sheet)
sh = gc.open('test_sheet')

# select the first sheet
wks = sh[0]

# update the first sheet with df, starting at cell B2.
wks.set_dataframe(df, (1,1))
