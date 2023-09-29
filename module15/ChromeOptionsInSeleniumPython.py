# How to Handle Chrome Options in Selenium-Python
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\chromedriver.exe")

# Invoking ChromeOptions
chromeOption = webdriver.ChromeOptions()

# applying some chromeOptions arguments example
# Run in headless mode (no GUI)
chromeOption.add_argument("--headless")
# disable developer mode extensions popup on selenium webdriver automation
chromeOption.add_argument("--disable-extensions")
# disable Browser notifications
chromeOption.add_argument("--disable-notifications")
# this flag is used to avoid invalid certificate warning while testing using self-signed or invalid
chromeOption.add_argument("--ignore-certificate-errors")

# Create a WebDriver instance with the specified Chrome Options
driver = webdriver.Chrome(service=service_obj, options=chromeOption)

# navigate to URL
driver.get("https://www.freshworks.com/")

# Apply static wait
time.sleep(5)

# fetching title of webPage
title = driver.title
print(title)

# Apply static wait
time.sleep(5)

# closing browser
driver.close()
