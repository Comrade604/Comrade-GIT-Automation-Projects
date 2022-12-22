from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

# Make a full screen
driver.maximize_window()

# Let's wait for the browser response in general
driver.implicitly_wait(30)

# Navigating to the Google Search website
driver.get('https://www.google.ca/')

# Checking that we're on the correct URL address and we're seeing correct title
if driver.current_url == 'https://www.google.ca/' and driver.title == 'Google':
    print(f'We\'re at Google homepage -- {driver.current_url}')
    print(f'We\'re seeing title message -- "Google.ca"')
    sleep(5)
    driver.close()
else:
    print(f'We\'re not at the Google homepage. Check your code!')
    driver.close()
    driver.quit()