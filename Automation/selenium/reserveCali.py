from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

int_list = []

for num in range(100000):
    nums = str(num).zfill(5)
    int_list.append(nums)

driver = webdriver.Chrome()
driver.get('https://tools.usps.com/zip-code-lookup.htm?citybyzipcode')
findZipButton = driver.find_element_by_xpath('//*[@id="tZip"]')


findZipButton.click()
findZipButton.send_keys('00501')
loginButton = driver.find_element_by_xpath('//*[@id="cities-by-zip-code"]')
loginButton.click() 
#outputButton = driver.find_element_by_xpath('//*[@id="cityByZipDiv" and @class="row col-md-5 col-sm-12 col-xs-12 recommended-cities"]').getText()
outputButton = driver.find_element_by_xpath('//*[@id="cityByZipDiv"]')
text_output = driver.find_element_by_class_name("row col-md-5 col-sm-12 col-xs-12 recommended-cities")
print(text_output)

"""

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
