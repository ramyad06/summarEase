import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

def scrape():
    base_url = "https://quotes.toscrape.com"
    url = "/page/1/"
    quotes = []

    while url:
        full_url = urljoin(base_url, url)
        print(f"Scraping: {full_url}")
        response = requests.get(full_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for ele in soup.find_all('div', class_='quote'):
            quote = ele.find('span', class_='text').text.lower()
            author = ele.find('small', class_='author').text.lower()
            quotes.append({'quote': quote, 'author': author})

        nxt_btn = soup.find('li', class_='next')
        if nxt_btn and nxt_btn.a:
            url = nxt_btn.a['href']
        else:
            url = None 

    filename = 'quotes.csv' #create the file
    with open(filename, 'w', newline='', encoding='utf-8') as f: #open the file
        w = csv.DictWriter(f, ['quote', 'author'])
        w.writeheader()
        for quote in quotes:
            w.writerow(quote)

if __name__ == "__main__":
    scrape()
