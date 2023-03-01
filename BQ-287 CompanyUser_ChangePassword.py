from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import BeeznestsLocators as locators

s = Service(executable_path='chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://test.beeznests.com/")


def Login():
    driver.find_element(By.XPATH, "//a[normalize-space()='LOG IN']").click()
    driver.find_element(By.ID, "email").send_keys("comrade604@gmail.com")
    sleep(1)
    driver.find_element(By.ID, "password").send_keys("12345678")
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/button").click()  # login button
    sleep(3)
    print(driver.current_url)
    if driver.current_url == "https://test.beeznests.com/":
        print("You have been successfully logged in to Beeznests.")
    else:
        print("Login failed.")


def Change_password():
    driver.find_element(By.XPATH, locators.DropDown_Menu).click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Change Password']").click()
    driver.find_element(By.XPATH, locators.Old_password).send_keys("12345678")
    driver.find_element(By.XPATH, locators.New_password).send_keys("123456789")
    driver.find_element(By.XPATH, locators.Confirm_new_password).send_keys("123456789")
    driver.find_element(By.XPATH, "//span[@class='v-btn__content']").click()
    sleep(3)
    print("Change password successful.")

def Change_password_back():
    driver.find_element(By.XPATH, locators.Old_password).send_keys("123456789")
    driver.find_element(By.XPATH, locators.New_password).send_keys("12345678")
    driver.find_element(By.XPATH, locators.Confirm_new_password).send_keys("12345678")
    driver.find_element(By.XPATH, "//span[@class='v-btn__content']").click()
    sleep(3)
    print("Changed password back.")


def Logout():
    driver.find_element(By.XPATH, "/html/body/div/div/header/div[1]/div/nav[2]/div/span/img").click()  # Dropdown menu
    sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/header/div[1]/div/nav[2]/div/div/div/span").click()  # Logout button
    sleep(2)
    print("You are logged out of Beeznests.")


def Login_with_new_password():
    driver.find_element(By.ID, "email").send_keys("comrade604@gmail.com")
    sleep(1)
    driver.find_element(By.ID, "password").send_keys("123456789")
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/button").click()  # login button
    sleep(3)
    print("Successfully logged in with new password.")


Login()
Change_password()
Logout()
Login_with_new_password()
Change_password_back()
Logout()
