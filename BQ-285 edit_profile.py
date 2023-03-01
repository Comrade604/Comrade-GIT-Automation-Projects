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


def Login():
    driver.find_element(By.XPATH, "//a[normalize-space()='LOG IN']").click()
    driver.find_element(By.ID, "email").send_keys("rashed.mahazi@gmail.com")
    sleep(2)
    driver.find_element(By.ID, "password").send_keys("123456789")
    sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/button").click()
    sleep(2)
    print(driver.current_url)
    if driver.current_url == "https://test.beeznests.com/":
        print("you have been successfully log in to Beeznests")
    else:
        print("Login failed")


def edit_profile():
    driver.find_element(By.XPATH, locators.Drop_Down).click()
    driver.find_element(By.XPATH, locators.Edit_profile).click()
    sleep(2)
    driver.find_element(By.XPATH, locators.Name).send_keys(Keys.CONTROL + "a")
    driver.find_element(By.XPATH, locators.Name).send_keys(Keys.BACKSPACE)
    sleep(2)
    driver.find_element(By.XPATH, locators.Name).send_keys("Ahmad Rashed Mahazi")
    sleep(1)
    driver.find_element(By.XPATH, locators.Introduction).send_keys(Keys.CONTROL + "a")
    driver.find_element(By.XPATH, locators.Introduction).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, locators.Introduction).send_keys("Full Stack Developer")
    sleep(1)
    driver.find_element(By.XPATH, locators.Linkedin).send_keys(Keys.CONTROL + "a")
    driver.find_element(By.XPATH, locators.Linkedin).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, locators.Linkedin).send_keys("Rashed Mahazi")
    sleep(1)
    driver.find_element(By.XPATH, locators.Add_Skills).click()
    sleep(2)
    driver.find_element(By.XPATH, locators.Graphic_Design).click()
    driver.find_element(By.XPATH, locators.Digital_Media).click()
    sleep(2)
    driver.find_element(By.XPATH, locators.Save).click()
    sleep(4)
    if driver.find_element(By.XPATH, "//div[@class='v-alert__content']").is_displayed():
        print("profile updated successfully")
    else:
        print("profile Update Failed")

    message = driver.find_element(By.XPATH, "//div[@class='v-alert__content']").text
    print(message)


Login()
edit_profile()