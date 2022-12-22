from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

# Make a full screen
driver.maximize_window()

# Let's wait for the browser response in general
driver.implicitly_wait(30)



# Navigating to the Moodle app website
driver.get('http://54.245.196.124/')

# Checking that we're on the correct URL address and we're seeing correct title
if driver.current_url == 'http://54.245.196.124/' and driver.title == 'SQA Server 1':
    print(f'We\'re at Moodle homepage -- {driver.current_url}')
    print(f'We\'re seeing title message -- "SQA Server 1"')
    sleep(5)
    driver.close()
else:
    print(f'We\'re not at the Moodle homepage. Check your code!')
    driver.close()
    driver.quit()