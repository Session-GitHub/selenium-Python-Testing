# Explicit Wait in Selenium

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
driver.get("https://the-internet.herokuapp.com/inputs")

# Apply static wait
time.sleep(5)

# applying Explicit Wait
wait = WebDriverWait(driver, 60)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@type='number']")))
# WebDriverWait(driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@type='number']")))
driver.find_element(By.XPATH, "//input[@type='number']").send_keys(10)

# Apply static wait
time.sleep(5)

# print message
print("Successfully Executed...")

# close the browser
driver.close()
