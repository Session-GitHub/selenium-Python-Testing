# How to invoke Chrome browser and load the Website to automate
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# the service class is for managing the starting and stopping of local drivers
service_obj = Service()

# initializing the Chrome browser
driver = webdriver.Chrome(service=service_obj)

# maximize the window
driver.maximize_window()

# Apply implicitWait and pageLoad timeout
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)

# navigating to a webPage
driver.get("https://www.google.com")

# Apply static wait
time.sleep(10)

