import datetime
import moodle_locators_Nov_30 as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
#driver=webdriver.Chrome("chromedriver.exe")
s = Service(executable_path='chromedriver')

driver = webdriver.Chrome(service=s)

# Fixture methods
def setup():
    #maximizing the screen
    driver.maximize_window()
    #wait for the browser to load up
    driver.implicitly_wait(30)
    #navigate to the moodle app website
    driver.get(locators.moodle_url)
    #checking that the url is addy is correct and that we are seeing the correct title
    if driver.current_url == locators.moodle_url and driver.title == 'SQA Server 1':
        print(f'We are at the correct homepage---{driver.current_url}')
        print(f'We are seeing the title---"SQA Server 1"')
    else:
        print("We are not at the correct homepage. Please check your code")
        driver.close()
        driver.quit()

def tearDown():
        if driver is not None:
            print(f'--------------')
            print(f'The test was completed at : {datetime.datetime.now()}')
            driver.close()
            driver.quit()

def log_in():
    if driver.current_url == locators.moodle_url:
        driver.find_element(By.LINK_TEXT,'Log in').click()
        if driver.current_url == locators.moodle_login_url:
            driver.find_element(By.ID,'username').send_keys(locators.moodle_username)
            sleep(.25)
            driver.find_element(By.ID,'password').send_keys(locators.moodle_password)
            sleep(.25)
            driver.find_element(By.ID,'loginbtn').click()
            if driver.title == 'Dashboard' and driver.current_url==locators.moodle_dashboard_url:
                assert driver.current_url==locators.moodle_dashboard_url
                print('Login is successful and the Dashboard is present')
            else:
                print('Dashboard is not present, try again. D\oh')

def log_out():
    driver.find_element(By.CLASS_NAME, 'usermenu').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT,'Log out').click()
    sleep(0.25)
    if driver.current_url==locators.moodle_url:
       print(f'Log out successfully at:{datetime.datetime.now()}')

def create_new_user():
    driver.find_element(By.LINK_TEXT, "Site administration").click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users')
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    # send fake data to create a new user
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, 'id_preference_auth_forcepasswordchange').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    sleep(0.25)
    Select(driver.find_element(By.ID,'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID,'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(0.25)
    driver.find_element(By.ID,'id_city').send_keys(locators.city)
    sleep(0.25)

    sleep(0.25)
    Select(driver.find_element(By.ID,'id_country')).select_by_visible_text('Canada')
    sleep(0.25)
    Select(driver.find_element(By.ID,'id_timezone')).select_by_visible_text('America/Vancouver')
    driver.find_element(By.ID,'id_description_editoreditable').send_keys(locators.description)
    sleep(0.25)
    driver.find_element(By.ID,'id_imagealt').send_keys(locators.pic_desc)
    sleep(0.25)
    driver.find_element(By.XPATH,'//a[contains(.,"Additional names")]').click()
    sleep(0.25)
    driver.find_element(By.ID,'id_firstnamephonetic').send_keys(locators.phonetic_firstname)
    sleep(0.25)
    driver.find_element(By.ID,'id_lastnamephonetic').send_keys(locators.phonetic_lastname)
    sleep(0.25)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.phonetic_middlename)
    sleep(0.25)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.phonetic_alternatename)
    sleep(0.25)
    #Using click for the interest drop-down menu
    driver.find_element(By.XPATH,'//a[contains(.,"Interests")]').click()
    #breakpoint()
    sleep(0.25)
    #Using a for loop input items from the list in locators file and populate the data
    for tags in locators.list_of_interests:
        driver.find_element(By.XPATH,'//div[3]/input').click()
        sleep(0.25)
        driver.find_element(By.XPATH,'//div[3]/input').send_keys(tags)
        sleep(0.25)
        driver.find_element(By.XPATH,'//div[3]/input').send_keys(Keys.ENTER)


    #breakpoint()
#    sleep(0.25)









    driver.find_element(By.ID, 'id_submitbutton').click()


    #Select(driver.find_element(By.ID,'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    #sleep(.25)
    #breakpoint()
# Calling the methods
#open the chrome browser
setup()
#login
log_in()
#create user
create_new_user()
#logout
log_out()

tearDown()