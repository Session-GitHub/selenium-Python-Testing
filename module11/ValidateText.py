# Get Attribute of values to validate dynamic texts on the browser

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
driver.get("https://the-internet.herokuapp.com/dropdown")

# Apply static wait
time.sleep(5)

# fetching text
textElement = driver.find_element(By.XPATH, "//div[@class='example']//h3")
actual_Text = textElement.text
print(actual_Text)
expected_Text = "Dropdown List"

# Validate text using if-else statement
# if expected_Text in actual_Text:
#     print("Validation Passed : Expected text is found on the webPage...")
# else:
#     print("Validation Failed : Expected text is not found on the webPage...")

# validating text using the assert keyword
assert expected_Text == actual_Text

# Apply static wait
time.sleep(5)

# print message
print("Successfully Executed...")

# close the browser
driver.close()