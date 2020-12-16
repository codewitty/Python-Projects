import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

products = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

count = 1

for i in products:
    item = i.find('h4', class_='card-title').text.strip('\n')
    price = i.find('h5').text
    print(f'{count}) Product: {item} Price: {price}')
    count = count + 1
    '''
    quoteTags = tag[i].find_all('a',class_='tag')
    for quote in quoteTags:
        print(quote.text)
    '''
