import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from IPython.display import display


url = 'https://www.akchabar.kg/ru/exchange-rates/'
pages = requests.get(url)
soup = BeautifulSoup(pages.text, 'lxml')
table1 = soup.find('table', id='rates_table')

title = table1.find_all('span', class_='dib')
title = [item.text for item in title]

headers = []

for i in title:
    headers.append(i)
    headers.append(i)

headers.insert(0, ' ')

# Создание датафрейма
mydata = pd.DataFrame(columns=headers)

# Создаем цикл для заполнения mydata
for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row

# Импортирую в csv
last_date = datetime.now().strftime('%d_%m_%Y')
mydata.to_csv(f'creation_date_{last_date}.csv', index=False)

# Считываем данные с файла csv
mydata2 = pd.read_csv(f'creation_date_{last_date}.csv')

display(mydata2.to_string().replace('.1', ' '))\



