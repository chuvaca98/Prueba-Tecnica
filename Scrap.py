from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://webscraper.io/test-sites/e-commerce/scroll'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Nombres

nm = soup.find_all('a', class_='title')

nombres = list()

count = 0

for i in nm:
    if count < 3:
        nombres.append(i.text)
    else:
        break
    count += 1

#Puntos

pc = soup.find_all('h4', class_='pull-right price')

precio = list()

count = 0
for i in pc:
    if count < 3:
        precio.append(i.text)
    else:
      break
    count += 1

df = pd.DataFrame({'Nombre': nombres,'Precio':precio})

df.to_csv('C.csv')
print(df)