import requests

def get_news(category):
    api_key = ''
    url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={api_key}'

    res = requests.get(url)
    data = res.json()
    
    if data['status'] == 'ok':
        articles = data['articles']
        
        for index, article in enumerate(articles[:10], start = 1):
            print(f"{index}. {article['title']} - {article['source']['name']}")
            print(f"   {article['description']}")
            print(f"   Read more: {article['url']}")
            print()
        else:
            print('Failed to fetch')
        
if __name__ == "__main__":
    category = input("Enter the news category (e.g., business, entertainment, sports): ").lower()
    get_news(category)