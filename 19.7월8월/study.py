import requests

url = "https://api.bithumb.com/public/ticker/all"
data = requests.get(url).json()['data']
for coin in data:
    print(coin)
    