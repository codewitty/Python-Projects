import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.latlong.net/category/national-parks-236-42.html'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

table = soup.find('table')
table_rows = table.find_all('tr')

output_rows = []
for tr in table_rows:
    columns = tr.find_all('td')
    output = []
    for column in columns:
        output.append(column.text)
    output_rows.append(output)

with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)
