# Extracting Text from webPage with Validation Assertions
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
driver.get("https://demo.midtrans.com/")

# Apply static wait
time.sleep(5)

# Validating the Text
expected_Text = "Midtrans Pillows"
actual_Text = driver.find_element(By.XPATH, "//div[@class='title']").text

# if expected_Text in actual_Text:
#     print("Validation Passed: Expected text found on the webPage...")
#
# else:
#     print("Validation Failed: Expected text not found on the webPage...")

# validating using assertion
assert expected_Text == actual_Text

# Apply static wait
time.sleep(5)

# print message
print("\nSuccessfully Executed...")

# closing the browser
driver.close()
driver.quit()