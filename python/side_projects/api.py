import requests, json

baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '012993441012'}
res = requests.get(baseUrl, params=parameters)
print(res.url)

content = res.content
nfo = json.loads(content)
print(type(nfo))

item = nfo['items']
item_nfo = item[0]
title = item_nfo['title']
brand = item_nfo['brand']

# API KEY SECTION 
baseUrl_weather = 'http://api.openweathermap.org/data/2.5/forecast'
parameters_w = {'APPID': '41e37c504e5c617ad37e51003aad84f4','q': 'Seattle, US'}

res = requests.get(baseUrl_weather, params=parameters_w)