#####################################
#            Test Case              #
# ###################################  
# Capture a keyword from a Google   #
# Sheet and push it to Trends and   #
# display trend data                #
#####################################

#####################################
# Import PyGSheets                  #
#####################################
# This import allows us to interact #
# with GSheets through Python       #
#####################################
import pygsheets

#####################################
# Import Pandas for Data Formatting |
#####################################
import pandas as pd 

#####################################
#  Initialize the PyTrends          |
#####################################

from pytrends.request import TrendReq 
pytrend = TrendReq()

#####################################
# GSheets Authorization             |
#####################################

gc = pygsheets.authorize(service_file='key/creds.json')

#####################################
# Open the GSheet destination file  |
#####################################

sh = gc.open('test_sheet')

#####################################
# Select the first sheet            |
#####################################

wks = sh[0]
wks2 = sh[1]

#####################################
# Update the first sheet with df,   |
# starting at cell B2.              |
#####################################
temp1 = wks.cell((3,1)).value
print(temp1)

pytrend.build_payload(kw_list=[temp1])
df = pytrend.interest_by_region()
df.head(10)
#print (df.head(15))
wks2.set_dataframe(df, (1,2))