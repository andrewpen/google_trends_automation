import requests

url1 = "https://api.linkedin.com//v2/learningAssets?assetFilteringCriteria.keyword=java&count=20&q=criteria&start=80"

url2 = "https://www.linkedin.com/oauth/v2/accessToken"
myobj1 = {'grant-type': 'client_credentials'}
myobj2 = {'client_id': '78br9a25210ukc'}
myobj3 = {'client_secret': 'OzZvS...'}
myobj4 = {'Content-Type': 'application/x-www-form-urlencoded'}

foo = requests.post(url2, data = myobj1)

#res = requests.get(url1)

print(foo.status_code)