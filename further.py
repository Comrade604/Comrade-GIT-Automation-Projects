import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service(executable_path='./chromedriver')

driver = webdriver.Chrome(service=s)


# Fixture method - to open web browser
def setUp():
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
    else:
        print(f'We\'re not at the Moodle homepage. Check your code!')
        driver.close()
        driver.quit()


def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


def log_in():
    if driver.current_url == 'http://54.245.196.124/':
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == 'http://54.245.196.124/login/index.php':
            driver.find_element(By.ID, 'username').send_keys('admin')
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys('Moodle$erver001!#')
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()
            if driver.title == 'Dashboard' and driver.current_url == 'http://52.245.196.124/my/':
                assert driver.current_url == 'http://54.245.196.124/my/'
                print(f'Log in successfully. Dashboard is present')
            else:
                print(f'We\re not at the Dashboard. Try again')


def log_out():
    driver.find_element(By.CLASS_NAME, 'usermenu').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Log out').click()
    sleep(0.25)
    if driver.current_url == 'http://54.245.196.124/':
        print(f'Log out successfully at: {datetime.datetime.now()}')

# Open web browser
setUp()
# Log in
log_in()
# Log out
log_out()
# Close the web browser
tearDown()