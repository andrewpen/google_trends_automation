import pandas as pd 
from pytrends.request import TrendReq
pytrend = TrendReq()

# Search specific terms
pytrend.build_payload(kw_list=['Taylor Swift'])
# Interest by region
df = pytrend.interest_by_region()
df.head(10)
print (df.head())

# Daily search trends
df = pytrend.trending_searches(pn='united_states')
df.head()
print (df.head())