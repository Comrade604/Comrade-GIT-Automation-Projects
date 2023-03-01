from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import BeeznestsLocators as locators

s = Service(executable_path='chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://test.beeznests.com/")


def registration():
    driver.find_element(By.XPATH, locators.Register_Tab).click()
    driver.find_element(By.ID, locators.Email_Address).send_keys("vajap61680@mustbeit.com")  # temporary email address
    driver.find_element(By.ID, locators.Password).send_keys("123456789")
    driver.find_element(By.ID, locators.Confirm_Password).send_keys("123456789")
    driver.find_element(By.XPATH, locators.Checkbox).click()
    driver.find_element(By.XPATH, locators.Register).click()

    breakpoint()
    #to be finish

registration()