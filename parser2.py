# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from IPython.display import display
import csv

url = 'https://www.akchabar.kg/ru/exchange-rates/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
table1 = soup.find('table', id='rates_table')

headers = []
items = table1.find('tbody').find_all('tr')

for item in items:
    headers.append(
        {
            "banks" : item.find('td').text,
                "usd_pokupka" : item.find_all('td')[1].text,
                "usd_prodaja" : item.find_all('td')[2].text,
                "eur_pokupka" : item.find_all('td')[3].text,
                "eur_prodaja" : item.find_all('td')[4].text,
                "rub_pokupka" : item.find_all('td')[5].text,
                "rub_prodaja" : item.find_all('td')[6].text,
                "kzt_pokupka" : item.find_all('td')[7].text,
                "kzt_prodaja" : item.find_all('td')[8].text,
        }
    )


last_date = datetime.now().strftime('%d_%m_%Y')

names = ["banks",
        'usd_pokupka',
        "usd_prodaja",
        "eur_pokupka",
        "eur_prodaja",
        "rub_pokupka",
        "rub_prodaja",
        "kzt_pokupka",
        "kzt_prodaja"]
with open(f'creation_date_{last_date}.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=names)
    writer.writeheader()
    writer.writerows(headers)

