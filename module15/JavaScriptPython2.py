# Execute JavaScript to interact with an element (e.g., click a button)
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
driver.get("https://www.renewbuy.com/")

# Apply static wait
time.sleep(5)

# using JavaScript click on an Element that is at the bottom of Page
element = driver.find_element(By.XPATH, "//a[contains(.,'Terms & Conditions')]")
# clicking on element(Terms & Conditions)
driver.execute_script("arguments[0].click();", element)

# Apply static wait
time.sleep(5)

# print message
print("Successfully Executed...")

# closing browser
driver.close()