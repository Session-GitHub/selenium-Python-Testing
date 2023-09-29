# How to invoke Edge browser and load the Website to automate
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

# the service class is for managing the starting and stopping of local drivers
service_obj = Service()

# initializing the Edge browser
driver = webdriver.Edge(service=service_obj)

# Maximize the Chrome browser
driver.maximize_window()

# Apply the implicitWait and PageLoad timeout
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)

# Navigating to the webPage
driver.get("https://www.google.com")

# getting the title
title = driver.title
print("Title is : ", title)

# getting the current URL
url = driver.current_url
print("Current URL is : ", url)

# Apply static wait
time.sleep(5)

# how to refresh the webPage
driver.refresh()

# Apply static wait
time.sleep(5)

# closing the browser
driver.close()
driver.quit()