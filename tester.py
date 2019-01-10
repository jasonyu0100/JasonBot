
import requests
import json

API_KEY = 'g1ubfI32am1y2bDQJxvWzf2xYR30CLMk'
URL = 'https://api.giphy.com/v1/gifs/search'

response = requests.get(URL,params={
    'api_key':API_KEY,
    'q':'cat',
})

print(json.dumps(response.json()['data'][0]['images']['original']['url'],indent="  "))
