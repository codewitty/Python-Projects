from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup




int_list = []

for num in range(100000):
    nums = str(num).zfill(5)
    int_list.append(nums)

output_list = []

driver = webdriver.Chrome()
for i in range(95050, 95055):
    driver.get('https://www.unitedstateszipcodes.org/')
    findZipBox = driver.find_element_by_xpath('/html/body/div/div/div[4]/div/form/div/div[2]/div/span[1]/input[2]')
    findZipBox.click()
    findZipBox.send_keys(i)
    zipSearchButton = driver.find_element_by_xpath('//*[@id="search-forms"]/div[2]/div/span[2]/button')
    zipSearchButton.click() 
    url = 'https://unitedstateszipcodes.org/' + str(i) + "/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    outputs = soup.find_all('table', class_='table table-condensed table-striped')
    for i in outputs:
        item = i.find('td').text.strip('\n')
        print(i) 

#outputButton = driver.find_element_by_xpath('//*[@id="cityByZipDiv" and @class="row col-md-5 col-sm-12 col-xs-12 recommended-cities"]').getText()
"""
#result = driver.findElement(By.xpath(".//*[@id='myTable']//td[contains(.,'Post Office City:')]")).getText();
outputButton = driver.find_element_by_xpath('//*[@id="cityByZipDiv"]')
text_output = driver.find_element_by_class_name("row col-md-5 col-sm-12 col-xs-12 recommended-cities")
print(text_output)


for i in int_list: 
    findZipButton.click()
    findZipButton.send_keys(i)
    loginButton = driver.find_element_by_xpath('//*[@id="cities-by-zip-code"]')
    loginButton.click() 
    findZipButton.clear()

wait = WebDriverWait(driver, 10)

loginButton.send_keys('gomesjoshua@gmail.com')

loginPass = driver.find_element_by_xpath('//*[@id="txtPassword"]')

loginButton2 = driver.find_element_by_xpath('//*[@id="divOnlyLogin"]')
loginButton2.click() 
"""
