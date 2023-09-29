# Techniques to handle Child Windows/Tabs with Selenium-Python

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
driver.get("https://the-internet.herokuapp.com/windows")

# Apply static wait
time.sleep(5)

# Handling Child Window & Tabs ----------------------------------------------------------------------
clickOnNewTabElement = driver.find_element(By.XPATH, "//div[@class='example']/a[contains(.,'Click Here')]")
clickOnNewTabElement.click()
time.sleep(5)

# handle the child tab
tabs = driver.window_handles
# switch to the child tab
driver.switch_to.window(tabs[1])
time.sleep(5)

actualText = driver.find_element(By.XPATH, "//div[@class='example']").text
expectedText = "New Window"
# verify the Text
assert expectedText in actualText

# switching on the parent Tab
driver.switch_to.window(tabs[0])

# Apply static wait
time.sleep(5)

# print message
print("Successfully Executed...")

# close the browser
driver.close()
