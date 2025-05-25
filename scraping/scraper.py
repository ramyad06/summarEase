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

        for row in soup.find_all('div', class_='quote'):
            quote = row.find('span', class_='text').text
            author = row.find('small', class_='author').text
            quotes.append({'quote': quote, 'author': author})

        next_button = soup.find('li', class_='next')
        if next_button and next_button.a:
            url = next_button.a['href']
        else:
            url = None 

    filename = 'quotes.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, ['quote', 'author'])
        w.writeheader()
        for quote in quotes:
            w.writerow(quote)

if __name__ == "__main__":
    scrape()
