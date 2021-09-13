import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from os.path import join, dirname
from dotenv import load_dotenv

#Loading .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

EMAIL = "sahil"
#os.environ.get("EMAIL")
PASSWORD = "123"
#os.environ.get("PASSWORD")

print(EMAIL)

# Using this to check if its the first time of the day or not
# Default initiated with True.
f = open("status_storage.txt", "r")
status = f.read()

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() +"/chromedriver"
print("sss",chrome_driver)

def keka_login():
    global f
    # webdriver.Chrome()

    # driver = webdriver.Chrome('./chromedriver')

    browser = webdriver.Chrome(executable_path=chrome_driver)
    print('Login Process Started: ')
    browser.get("url")
    print('Website Opened')

    time.sleep(5)

    # email = browser.find_element_by_xpath('//*[@id="email"]')
    # email.send_keys(EMAIL)
    # print('Email Entered')

    email = browser.find_element_by_xpath('//*[@id="email"]')
    email.send_keys(EMAIL)
    print('Email Entered')


    # password = browser.find_element_by_xpath('//*[@id="password"]')
    # password.send_keys(PASSWORD)
    # print('Password Entered')


    time.sleep(5)

    login_button = browser.find_element_by_xpath('//*[@id="login-container-center"]/div/div/form/div/div[2]/div/button')
    login_button.click()
    print('Login Button Clicked')

    # wait = WebDriverWait(webdriver.Chrome(), 10)
    # wait.until(lambda driver: driver.current_url != "url")

    time.sleep(5)

    password = browser.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(PASSWORD)
    print('Password Entered')

    login_button = browser.find_element_by_xpath('//*[@id="login-container-center"]/div/div/form/div/div[4]/div/button')
    login_button.click()
    print('Login Button Clicked Main')

    # web_clockin_button = browser.find_element_by_xpath('//*[@id="attendance-widget"]/div/div[2]/div/div[1]/div[2]/input[1]')
    # web_clockin_button.click()
    # print('Clicked WebClock In')


    


    # location_request_button = browser.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div/div[3]/button')
    # location_request_button.click()
    # print('Location Request Declined')


    # if status == 'True':
    #     note_text_area = browser.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div/div[2]/form/div[1]/div/textarea')
    #     note_text_area.send_keys("Starting now")
    #     print('Entered Description')


    #     time.sleep(5)

    #     request_button = browser.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div/div[2]/form/div[2]/div/div/input[1]')
    #     request_button.click()
    #     print('Clicked Request Button')


    time.sleep(10)
    print('Successfully logged in')
    # f.close()
    # f = open("status_storage.txt", "w")
    # f.write("False")
    # f.close()
    # print (time.strftime("Cron Successfully ran last at: " + "%Y-%m-%d %H:%M"))
    # browser.quit()

    browser.get("url")
    print('Attendance navigate logged in')


    time.sleep(30)
keka_login()
