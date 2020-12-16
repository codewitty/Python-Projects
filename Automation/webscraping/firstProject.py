import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

quotes = soup.find_all('span', class_='text')
author = soup.find_all('small', class_='author')
tag = soup.find_all('div', class_='tags')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(author[i].text)
    quoteTags = tag[i].find_all('a',class_='tag')
    for quote in quoteTags:
        print(quote.text)
