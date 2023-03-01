from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://test.beeznests.com/new-login')
assert driver.find_element(By. XPATH, '/html/body/div/div/div[1]/div[1]/h2').is_displayed()
print("passed")
driver.find_element(By.ID, 'email').send_keys('comrade604@gmail.com')
driver.find_element(By.ID, 'password').send_keys('12345678')
driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[1]/button/span').click()
driver.find_element(By.XPATH, '/html/body/div/header/div[1]/div/nav[1]/a[1]/span').click()
assert driver.find_element(By.XPATH, '/html/body/div/div[1]/div[4]/div[3]/h3/span[2]').is_displayed()
print("The project is present on the projects page.")
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[4]/div[3]/div[4]/a[2]/span').click() # "View More" button
driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div[2]/div').click() # "delete" icon
#if driver.current_url == "https://test.beeznests.com/new-projects":
    #print("The project has been successfully deleted and the user redirected to the login page.")
#else:
    #print("Automation failed!")

driver.close()
driver.quit()

