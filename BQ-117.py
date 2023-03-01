# BQ-117 Testing Beeznests front page response and load time

# Importing packages and methods
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

# Defining parameters
s = Service(executable_path='chromedriver.exe')

driver = webdriver.Chrome(service=s)

# Loading Beeznest site
driver.get('https://test.beeznests.com')

# Checking page response status codes and printing them to the console
for request in driver.requests:
    if request.response:
        print(
            request.url,
            request.response.status_code,
            request.response.headers['Content-Type']
        )

# Checking that we're on the correct URL address and we're seeing correct title
if driver.current_url == 'https://test.beeznests.com/' and driver.title == 'Beeznests':
    print(f'We\'re at Beeznests -- {driver.current_url}')
    print(f'We\'re seeing title message -- "Beeznests"')
    sleep(2)
    driver.close()
else:
    print(f'We\'re not at the correct homepage. Check your code!')
    driver.close()
    driver.quit()