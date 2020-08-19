import pandas as pd 
from pytrends.request import TrendReq
pytrend = TrendReq()

#################################
##### Search specific terms #####
#################################

# pytrend.build_payload(kw_list=['Taylor Swift'])

##### Interest by region #####

# df = pytrend.interest_by_region()
# df.head(10)
# print (df.head(15))

#########################
##### Plot the data #####
#########################

#df.reset_index().plot(x='geoName', y='Taylor Swift', figsize=(120, 10),kind='bar')

###############################
##### Daily search trends #####
###############################

# df = pytrend.trending_searches(pn='united_states')
# df.head()
# print (df.head())

# df = pytrend.today_searches(pn='US')
# print (df)

######################
##### Top Charts #####
######################

##### Get Google Top Charts #####

# df = pytrend.top_charts(2019, hl='en-US', tz=300, geo='GLOBAL')
# df.head()
# print (df)

##########################################
##### Get Google Keyword Suggestions #####
##########################################

# keywords = pytrend.suggestions(keyword='Mercedes Benz')
# df = pd.DataFrame(keywords)
# df.drop(columns='mid') # This column makes no sense
# print (df)

###############################
##### Get Related Queries #####
###############################

#pytrend.build_payload(kw_list=['Coronavirus'])

##### Related Queries, returns a dictionary of dataframes #####

# related_queries = pytrend.related_queries()
# print(related_queries.values())

##### Related Topics, returns a dictionary of dataframes #####

# related_topic = pytrend.related_topics()
# print(related_topic.values())