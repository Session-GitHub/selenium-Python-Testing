# Finding web Elements using the XPath
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

# the service class is for managing the starting and stopping of local drivers
service_obj = Service()

# initializing the Chrome browser
driver = webdriver.Chrome(service=service_obj)

# Maximizing the browser
driver.maximize_window()

# Apply implicitly wait and PageLoad Timeout
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)

# Apply static wait
time.sleep(5)

# navigate to URL
driver.get("https://www.google.com")

# Apply static wait
time.sleep(5)

# locating search box using XPath
driver.find_element(By.XPATH, "//textarea[@name='q']").send_keys("How to find web Elements using CSS Selector")
driver.find_element(By.XPATH, "//textarea[@name='q']").send_keys(Keys.ENTER)

# Apply static wait
time.sleep(5)

# print a message
print("Successfully Executed...")

# close the browser
driver.close()
driver.quit()