#####################################
# Import PyGSheets                  #
#####################################
# This import allows us to interact #
# with GSheets through Python       #
#####################################
import pygsheets

#####################################
# Import Pandas for Data Formatting #
#####################################
import pandas as pd 

#####################################
# GSheets Authorization             #
#####################################
gc = pygsheets.authorize(service_file='key/creds.json')

#####################################
# Create empty dataframe for the    #
# temp data                         #
#####################################
df = pd.DataFrame()

#####################################
# Create a column to hold the       #
# temp data                         #
#####################################
df['Name'] = ['Andrew', 'Ryan', 'Kris']

#####################################
# Display the temp data to make     #
# sure we're all good               #
#####################################
print(df['Name'])

#####################################
# Open the GSheet destination file  #
#####################################
sh = gc.open('test_sheet')

#####################################
# Select the first sheet            #
#####################################
wks = sh[0]

#####################################
# Update the first sheet with df,   #
# starting at cell B2.              #
#####################################
wks.set_dataframe(df, (1,1))

#####################################
# Success!                          #
##################################### 
print("Success!")