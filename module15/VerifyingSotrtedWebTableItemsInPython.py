# How to Sort the Web tables using Selenium Python
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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# Apply static wait
time.sleep(5)

# to store items after clicking
oldSortedItems = []

# click on veg/fruitName element
driver.find_element(By.XPATH, "//span[contains(.,'Veg/fruit name')]").click()

# collect all veg/fruitName after sorted by clicking
afterClickingElement = driver.find_elements(By.XPATH, "//tr//td[1]")
for item in afterClickingElement:
    oldSortedItems.append(item.text)

# copy all sorted items in another list
newSortedItems = oldSortedItems.copy()
print(newSortedItems)

# sorted the oldSortedItems
oldSortedItems.sort()

# verify the sorted Lists
assert newSortedItems == oldSortedItems

# Apply static wait
time.sleep(5)

# print message
print("Successfully Executed...")

# closing browser
driver.close()