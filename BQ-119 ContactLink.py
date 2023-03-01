from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Create an instance of the web driver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the webpage that contains the mailto link
driver.get("https://test.beeznests.com/")

driver.find_element(By.XPATH, "//body").send_keys(Keys.END)

# Locate the mailto link on the webpage
mailto_link = driver.find_element(By.LINK_TEXT, "Contact Us")

assert mailto_link.is_displayed()

href_value = mailto_link.get_attribute("href")

expected_url = "mailto:jin.liu@beeznests.com"

assert href_value == expected_url

if href_value == expected_url:
    print("The email link is correct:")
    print(href_value)
else:
    print("Email validation failed.")

driver.quit()