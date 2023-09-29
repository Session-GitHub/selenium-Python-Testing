# Handling AutoSuggestive Dynamic dropdowns using Selenium Webdriver

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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

# navigate to URL for select item from Drop Down List
driver.get("https://the-internet.herokuapp.com/dropdown")

# Apply static wait
time.sleep(5)

# Dynamic dropDownList item
driver.find_element(By.XPATH, "//select[@id='dropdown']").click()
# Apply static wait
time.sleep(5)
# clicking on the desired option
driver.find_element(By.XPATH, "//option[contains(text(),'Option 2')]").click()

# Apply static wait
time.sleep(5)


# Apply static wait
time.sleep(5)

# print message
print("Successfully Executed...")

# close the browser
driver.close()
