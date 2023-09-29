# Handling CheckBox dynamically using Selenium Python programming

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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Apply static wait
time.sleep(5)

# Handling checkBox
checkBoxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# checking and un-checking checkboxes
checkBoxes[0].click()
time.sleep(3)
checkBoxes[1].click()
time.sleep(3)
checkBoxes[2].click()
time.sleep(3)
checkBoxes[2].click()
time.sleep(3)
checkBoxes[1].click()
time.sleep(3)
checkBoxes[0].click()

# Apply static wait
time.sleep(5)

# print message
print("Successfully Executed...")

# close the browser
driver.close()

