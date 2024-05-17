import threading, requests, time
from bs4 import BeautifulSoup
from datetime import datetime
from tqdm import tqdm 

class ProgressThread(threading.Thread):
    def __init__(self):
        super().__init__
        self.value = 0

def fetch_hn(prog):
    url= 'https://news.ycombinator.com/'
    print(f'\nFetching top 5 threads from {url}')

    res = requests.get(url)

    if res.status_code != 200:
        print(f"Failed to fetch page content of {url}. Status code: {res.status_code}")
        return
    
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.find_all('tr', class_='athing')[:5]
    
    with tqdm(total=len(articles), desc="Hacker News Progress") as pbar:
        for index, article in enumerate(articles, start=1):
            title_element = article.find('span', class_='titleline')
            title = title_element.text if title_element else "Title not found"
            url_element = title_element.find('a') if title_element else None
            url = url_element['href'] if url_element else "URL not found"
            print(f'\n{index}. {title} - {url}')
            pbar.update(1)
    
def fetch_mta(prog):
    url = 'https://www.malware-traffic-analysis.net/2024/index.html'
    print(f'\nFetching this months content from {url}')
    
    res = requests.get(url)
    
    if res.status_code != 200:
        print(f"Failed to fetch page content of {url}. Status code: {res.status_code}")
        return
    
    soup = BeautifulSoup(res.text, 'html.parser')
    
    current_month = datetime.now().strftime('%Y-%m')
    ul = soup.find('ul')
    items = ul.find_all('li')[:5]  # Get the top 5 list items
       
    with tqdm(total=len(items), desc="Malware Traffic Analysis Progress") as pbar:
        for index, item in enumerate(items, start=1):
            date_link = item.find('a', class_='list_header')
            post_link = item.find('a', class_='main_menu')
            
            if date_link and post_link:
                date = date_link.text.strip()
                if date.startswith(current_month):
                    title = post_link.text.strip()
                    url = post_link['href']
                    full_url = f'https://www.malware-traffic-analysis.net/2024/{url}'
                    print(f'\n{index}. {date} - {title} - {full_url}')
                    pbar.update(1)

if __name__ == "__main__":
        
    hn_thread = threading.Thread(target=fetch_hn, args=(ProgressThread(),))
    hn_thread.start()
    
    mta_thread = threading.Thread(target=fetch_mta, args=(ProgressThread(),))
    mta_thread.start()
        
    hn_thread.join()
    mta_thread.join()

    print('All threads have finished.')