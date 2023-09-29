# Handling Java / JavaScript Alert popups using Selenium

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

# Handling PopUp ---------------------------------------------------------------------------
name = "Piyush Verma"
driver.find_element(By.XPATH, "//input[@id='name']").send_keys(name)
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()

# driver has no knowledge about PopUp so, switch browserMode to alertMode
alert = driver.switch_to.alert
actual_Text = alert.text
expected_Text = 'Hello ' + name + ', share this practice page and share your knowledge'

# validating PopUp message
assert expected_Text in actual_Text

# Apply static wait
time.sleep(5)

# accepting PopUp
alert.accept()

# Apply static wait
time.sleep(5)

# print message
print("Successfully Executed...")

# close the browser
driver.close()