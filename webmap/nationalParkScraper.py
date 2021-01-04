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
with open('final_np.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['National Park Name','State','County','Location','Co-ordinates','Area','Visitors','Date','Nearest Cities'])
    writer.writerows(output_rows)

