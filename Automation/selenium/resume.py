from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://codewitty.github.io/resume/')

messageField = driver.find_element_by_xpath('/html/body/div[4]/div[1]/a')
messageField.click() 

name = driver.find_element_by_xpath('/html/body/div[2]/form/input[1]')
name.send_keys('James Schwartx')

email = driver.find_element_by_xpath('/html/body/div[2]/form/input[2]')
email.send_keys("born2codetech@gmail.com")

message = driver.find_element_by_xpath('/html/body/div[2]/form/textarea')
message.send_keys("This is a test email. I\'m learning how to use python and become a true Python master.")

showMessageButton = driver.find_element_by_xpath('/html/body/div[2]/form/input[3]')
showMessageButton.click() 
