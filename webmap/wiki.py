import requests
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

tables = soup.find('table',class_="wikitable sortable")
table_rows = tables.find_all('tr')
count = 0
for row in table_rows:
    count+=1
    print(row)
NoneType = type(None)
print(count)

output_rows = []
for row in table_rows:
    names = row.find('th',{'scope':'row'})
    names2 = row.find('td',{'scope':'row'})
    lat = row.find('span',class_="latitude")
    lng = row.find('span',class_="longitude")
    outputs=[]
    if type(names) != NoneType:
        outputs.append(names.text.rstrip())
    elif type(names2) != NoneType:
        outputs.append(names2.text.rstrip())
    elif type(lat) != NoneType:
        outputs.append(lat.text)
    elif type(lng) != NoneType:
        outputs.append(lng.text)
    elif outputs:
        output_rows.append(outputs)
print(output_rows)


"""
for name, lats, lngs in zip(names,lat,lng):
    outputs=[]
    outputs.append(name.text.rstrip())
    outputs.append(lats.text)
    outputs.append(lngs.text)
    output_rows.append(outputs)
print(output_rows)

with open('outputNew.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)
"""
