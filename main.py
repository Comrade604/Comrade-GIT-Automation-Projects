from selenium import webdriver
driver=webdriver.Chrome("chromedriver")
driver.maximize_window()
driver.implicitly_wait(30)