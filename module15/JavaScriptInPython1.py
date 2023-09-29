# Execute JavaScript to scroll to the bottom of the page
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# creating object of Service Class, (the service class is for managing the starting and stopping of local drivers)
service_obj = Service()

# initializing the Chrome Browser
driver = webdriver.Chrome(service=service_obj)

# maximizing the Chrome Browser window
driver.maximize_window()

# Apply implicitly and PageLoadTimeout wait
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)

# Apply static wait
time.sleep(5)

# Navigate to a URL
driver.get("https://www.renewbuy.com/")

# Apply static wait
time.sleep(5)

# Scrolling down using JavaScript
# driver.execute_script("window.scrollBy(0, 500);")
# driver.execute_script("window.scrollBy(0, 1000);")
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

# Apply static wait
time.sleep(5)

# print a message
print("Successfully Executed...")

# close the web Browser
driver.close()