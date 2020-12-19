from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.reservecalifornia.com/CaliforniaWebHome/')

loginButton = driver.find_element_by_xpath('//*[@id="aLogin"]')
loginButton.click() 

wait = WebDriverWait(driver, 10)

loginButton = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="txtUserName"]')))
loginButton.send_keys('gomesjoshua@gmail.com')

loginPass = driver.find_element_by_xpath('//*[@id="txtPassword"]')
loginPass.send_keys('YLn#3G9tnbExtXw')

loginButton2 = driver.find_element_by_xpath('//*[@id="divOnlyLogin"]')
loginButton2.click() 
