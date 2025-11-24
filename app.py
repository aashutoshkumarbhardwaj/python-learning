import threading
from bs4 import BeautifulSoup
import requests

urls=[ 
    'https://poetistic.com/sher',
    'https://poetistic.com/writers',
    'https://poetistic.com/quotes',

]

def fetch_url(url):
    response = requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f"Fetched {len(soup.text)} with title: {url}")

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All URLs have been fetched.")


