# Identifying Static dropdowns using Select class of selenium
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# creating object of Service Class, (the service class is for managing the starting and stopping of local drivers)
service_obj = Service()

# initializing the Chrome Browser
driver = webdriver.Chrome(service=service_obj)

# Maximizing the Browser
driver.maximize_window()

# Apply implicitly and PageLoadTimeout
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)

# Apply static wait
time.sleep(5)

# Navigating to the URl
driver.get("https://the-internet.herokuapp.com/dropdown")

# Apply static wait
time.sleep(5)

# static DropDownList
dropDownListItem = Select(driver.find_element(By.XPATH, "//select[@id='dropdown']"))
# dropDownListItem.select_by_index(1)
# dropDownListItem.select_by_value("2")
dropDownListItem.select_by_visible_text("Option 1")

# Apply static wait
time.sleep(5)

# print a message
print("Successfully Executed...")

# close the Browser
driver.close()