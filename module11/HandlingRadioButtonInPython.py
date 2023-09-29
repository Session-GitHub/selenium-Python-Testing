# Understand radioButton Automation methods with examples

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

# navigate to URL
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Apply static wait
time.sleep(5)

# XPath for radioButtonOptions
radio_buttons = driver.find_elements(By.XPATH, "//input[@class='radioButton']")
selectingRadioButtonOptions = ["radio1", "radio2", "radio3"]

# selecting option
for option in radio_buttons:
    if option.get_attribute("value") == selectingRadioButtonOptions[2]:
        option.click()
        assert option.is_selected()
        break

# Apply static wait
time.sleep(5)

# print message
print("Successfully Executed...")

# close the browser
driver.close()