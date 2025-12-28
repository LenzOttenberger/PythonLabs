import requests_cache
from bs4 import BeautifulSoup
import time
import csv

session = requests_cache.CachedSession(
    'Wikipedia_Countries_Cache',
    expire_after=3600,
    backend='sqlite'
)
session.headers.update({
    'User-Agent': 'My User Agent 1.0 Chrome/143.0.7499.170',
    'From': 'Kirill.Drozd15@gmail.com'
})

pages = []
url = 'https://en.wikipedia.org/wiki/'

countries = None
with open('countries.txt', 'r') as file:
    countries = [country.strip().replace(' ', '_') for country in file]
    
for country in countries:
    try:
        response = session.get(f'{url}{country}')
        print(response.status_code)
        pages.append(response.text)
    except ConnectionError:
        print('Connection Error!')
    except TimeoutError:
        print('Timeout Error!')
    time.sleep(1)
    
with open('countries.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    for page in pages:
        soup = BeautifulSoup(page, 'html.parser')
        country = soup.find('span', class_='mw-page-title-main').get_text()
        block = soup.find('table', class_='infobox ib-country vcard').find('tbody')
        capital = block.find('th', lambda tag: any('capital' in s.lower() for s in tag), class_='infobox-label').find_next_sibling('td').find('a').get_text(strip=True)
        area = block.find('div', string=lambda s: s and 'total' in s.lower()).parent.find_next_sibling('td').contents[0].replace(',', '').replace('&nbsp;km', '').replace('km', '').strip()
        population = block.contents[31].find('td', class_='infobox-data').contents[1].strip().replace(',', '')
        print(country, capital, area, population)
        writer.writerow([country, capital, area, population])
    
    




