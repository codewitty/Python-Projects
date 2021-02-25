import requests
from bs4 import BeautifulSoup

int_list = []

for num in range(100000):
    nums = str(num).zfill(5)
    int_list.append(nums)

for i in range(95050, 95055):
    url = 'https://unitedstateszipcodes.org/' + str(i) + "/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    outputs = soup.find_all('table', class_='table table-condensed table-striped')
    for i in outputs:
        item = i.find('td').text.strip('\n')
        print(i) 

