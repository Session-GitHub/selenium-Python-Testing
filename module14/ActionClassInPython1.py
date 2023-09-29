# Advanced Interactions with Browser elements using Actions class
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Creating object of Service Class,(the service class is for managing the starting and stopping of local drivers)
service_obj = Service()

# initializing the Chrome Browser
driver = webdriver.Chrome(service=service_obj)

# Maximizing the Chrome Browser
driver.maximize_window()

# Apply implicitly and PageLoadTimeout wait
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)

# Apply static wait
time.sleep(5)

# navigating to the URL
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Apply static wait
time.sleep(5)

# Action Class
action = ActionChains(driver)
hoveringElement = driver.find_element(By.XPATH, "//button[@id='mousehover']")

# clicking on Top Element
# topElement = driver.find_element(By.XPATH, "//div[@class='mouse-hover-content']/a[contains(.,'Top')]")
# action.move_to_element(hoveringElement).move_to_element(topElement).click().perform()

# clicking on Reload Element
reloadElement = driver.find_element(By.XPATH, "//div[@class='mouse-hover-content']/a[contains(.,'Reload')]")
action.move_to_element(hoveringElement).move_to_element(reloadElement).click().perform()

# Apply static wait
time.sleep(5)

# closing Chrome Browser
driver.close()
