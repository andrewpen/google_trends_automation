import requests

url = "https://api.linkedin.com//v2/learningAssets?assetFilteringCriteria.keyword=java&count=20&q=criteria&start=80"
res = requests.get(url)

print(res.status_code)