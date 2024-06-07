import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
res = requests.get(url)
sp = BeautifulSoup(res.text, 'lxml')

quotes = sp.find_all('span', class_='text')
authors = sp.find_all('small', class_='author')
tags = sp.find_all('div', class_='tags')


for _ in range(0, len(quotes)):
	print(quotes[_].text)
	print(authors[_].text)
	quoteTags = tags[_].find_all('a', class_='tag')

	for qt in quoteTags:
		print(qt.text)