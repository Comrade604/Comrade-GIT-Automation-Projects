from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import BeeznestsLocators as locators

s = Service(executable_path='chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://test.beeznests.com/")


def Login():
    driver.find_element(By.XPATH, "//a[normalize-space()='LOG IN']").click()
    driver.find_element(By.ID, "email").send_keys("comrade604@gmail.com")
    sleep(2)
    driver.find_element(By.ID, "password").send_keys("12345678")
    sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/button").click()
    sleep(2)
    print(driver.current_url)
    if driver.current_url == "https://test.beeznests.com/":
        print("You have been successfully logged in to Beeznests.")
    else:
        print("Login failed.")


def Logout():
    driver.find_element(By.XPATH, locators.DropDown_Menu).click()  # Dropdown menu
    sleep(2)
    driver.find_element(By.XPATH, locators.Logout_button).click()  # Logout button
    sleep(2)
    print("You are logged out from Beeznests.")


Login()
Logout()
