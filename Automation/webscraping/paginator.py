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

pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')

for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)

for link in urls:
    visitPage = url + link
    responses = requests.get(visitPage)
    soup = BeautifulSoup(response.text, 'lxml')

    products = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for i in products:
        item = i.find('h4', class_='card-title').text.strip('\n')
        price = i.find('h5').text
        print(f'{count}) Product: {item} Price: {price}')
        count = count + 1

