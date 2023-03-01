from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
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
    driver.find_element(By.ID, "email").send_keys("admin@beeznests.com")
    sleep(1)
    driver.find_element(By.ID, "password").send_keys("12345678")
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/button").click()  # login button
    sleep(3)
    print(driver.current_url)
    if driver.current_url == "https://test.beeznests.com/":
        print("you have been successfully log in to Beeznests")
    else:
        print("Login failed")


def PostProject():
    driver.find_element(By.XPATH, locators.PROJECTS).click()  # Project tab
    driver.find_element(By.XPATH, locators.Post_A_New_Project).click()
    driver.find_element(By.XPATH, locators.position).send_keys("Software Developer")  # Position Type
    sleep(2)
    driver.find_element(By.XPATH, locators.ProjectName).send_keys("Enjoy Dude")  # Project/Company Name
    driver.find_element(By.XPATH, locators.category).click()  # Category
    driver.find_element(By.XPATH, locators.Cloud_Computing_Engineers).click()
    bar = driver.find_element(By.XPATH, "//div[@class='v-slider__thumb primary']")
    ActionChains(driver).click_and_hold(bar).pause(1).move_by_offset(230, 0).release().perform()  # move the slider
    driver.find_element(By.XPATH, locators.AppDeadline).click()  # Application Deadline
    sleep(3)
    driver.find_element(By.XPATH, locators.Day).click()  # selecting the day in the calendar 23
    # filling the fields
    driver.find_element(By.XPATH, "(//p)[2]").send_keys(locators.Project_Description)
    driver.find_element(By.XPATH, "(//p)[4]").send_keys(locators.what_you_will_do)
    driver.find_element(By.XPATH, "(//p)[6]").send_keys(locators.Skills)
    driver.find_element(By.XPATH, "(//p)[8]").send_keys(locators.who_you_work_with)
    driver.find_element(By.XPATH, "(//p)[10]").send_keys(locators.Experience)
    driver.find_element(By.XPATH, "(//p)[12]").send_keys(locators.Key_practical_skills)

    driver.find_element(By.XPATH, "//span[normalize-space()='next']").click()  # first Next Button
    driver.find_element(By.XPATH, locators.second_next_button).click()
    sleep(2)
    driver.find_element(By.XPATH, "(//span[@class='v-btn__content'])[1]").click()  # save button


Login()
PostProject()
