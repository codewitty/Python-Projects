import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.mapsofworld.com/usa/national-parks/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

tables = soup.find_all('tr')
count = 0
output_rows = []
for row in tables:
    count+=1
    if count < 5:
        continue
    column = row.find_all('td')
    outputs=[]
    for part in column:
        outputs.append(part.text)
    output_rows.append(outputs)
    if count > 62:
        break
with open('final.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

"""
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
