import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
res = requests.get(url)
sp = BeautifulSoup(res.text, 'lxml')

items = sp.find_all('div', class_='col-lg-4 col-md-6 mb-4')
c = 1

for _ in items:
	itemName = _.find('h4', class_='card-title').text.strip('\n')
	itemPrice = _.find('h5').text
	#print(f'{c}). Price: {itemPrice}, Item Name: {itemName}')
	c = c + 1

pgs = sp.find('ul', class_='pagination')
urls = []
links = pgs.find_all('a', class_='page-link')

for l in links:
	page_num = int(l.text) if l.text.isdigit() else None
	if page_num != None:
		x = l.get('href')
		urls.append(x)
print(urls)
for _ in urls:
	new_url = url + _
	res = requests.get(new_url)
	sp = BeautifulSoup(res.text, 'lxml')
	items = sp.find_all('div', class_='col-lg-4 col-md-6 mb-4')
	c = 1
	for _ in items:
		itemName = _.find('h4', class_='card-title').text.strip('\n')
		itemPrice = _.find('h5').text
		print(f'{c}). Price: {itemPrice}, Item Name: {itemName}')
		c = c + 1