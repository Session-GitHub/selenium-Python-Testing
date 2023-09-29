# Advanced Interactions with Browser elements using Actions class

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Creating object of Service Class, (the service class is for managing the starting and stopping of local drivers)
service_obj = Service()

# initializing the Chrome browser
driver = webdriver.Chrome(service=service_obj)

# Maximizing the browser
driver.maximize_window()

# Apply implicitly wait and PageLoadTimeout
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)

# Apply static wait
time.sleep(5)

# navigate to URL
driver.get("https://the-internet.herokuapp.com/hovers")

# Apply static wait
time.sleep(5)

# Actions class ---------------------------------------------------------------------------


# Apply static wait
time.sleep(5)

# print message
print("Successfully Executed...")

# close the browser
driver.close()
