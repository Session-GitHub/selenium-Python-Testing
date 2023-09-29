# techniques to handle with Selenium-Python

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
driver.get("https://the-internet.herokuapp.com/")

# Apply static wait
time.sleep(5)

# switching to Frame webPage
driver.find_element(By.XPATH, "(//div[@id='content']//a[contains(.,'Frames')])[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[contains(.,'iFrame')]").click()
time.sleep(5)

# switching to a frame
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.XPATH, "//body[@id='tinymce']").clear()
driver.find_element(By.XPATH, "//body[@id='tinymce']").send_keys("Hiii, Now I am inside the Frame...")

# switching out from the Frame
driver.switch_to.default_content()

# Apply static wait
time.sleep(5)

# print message
print("Successfully Executed...")

# close the browser
driver.close()
