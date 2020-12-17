from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World')

showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click() 

inputField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
inputField1.send_keys('16')

inputField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
inputField2.send_keys('69')

getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotalButton.click() 
