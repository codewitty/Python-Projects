import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.latlong.net/category/national-parks-236-42.html'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

table = soup.find('table')
table_rows = table.find_all('tr')

output_rows = []
outputs = []
for tr in table_rows:
    headers = tr.find_all('th')
    columns = tr.find_all('td')
    output = []
    for header in headers:
        outputs.append(header.text)
    for column in columns:
        output.append(column.text)
    if not output:
        continue
    output_rows.append(output)
output_rows.insert(0,outputs)

with open('outputH.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)
