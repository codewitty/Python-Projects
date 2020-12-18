from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.reservecalifornia.com/CaliforniaWebHome/')

# storing the current window handle to get back to dashbord
main_page = driver.current_window_handle

print(driver.window_handles)

loginButton = driver.find_element_by_xpath('//*[@id="aLogin"]')
loginButton.click() 

# changing the handles to access login page
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle

driver.switch_to.window(login_page)

loginCred = driver.find_element_by_xpath('//*[@id="txtUserName"]')
loginCred.send_keys('gomesjoshua@gmail.com')

loginPass = driver.find_element_by_xpath('//*[@id="txtPassword"]')
loginPass.send_keys('YLn#3G9tnbExtXw')

loginButton2 = driver.find_element_by_xpath('//*[@id="divOnlyLogin"]')
loginButton2.click() 
