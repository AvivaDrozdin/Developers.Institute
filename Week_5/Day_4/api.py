import requests
# import json

resp = requests.get("https://api.chucknorris.io/jokes/random")

data = resp.json()

print(data['value'])

