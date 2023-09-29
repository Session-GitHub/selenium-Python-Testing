# selecting a Product from list of product and check whether it is added to the cart or not, and then we purchase it and then verify that product is successfully ordered
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Creating the object of service class,(the srvice class is for managing the starting and stopping of local drivers)
service_obj = Service()

# initializing the Chrome Browser
driver = webdriver.Chrome(service=service_obj)

# Maximizing the Browser window
driver.maximize_window()

# Apply implicitly and pageLoadTimeout wait
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)

# Apply the static wait
time.sleep(5)

# navigating to the URL for purchasing a product
driver.get("https://rahulshettyacademy.com/angularpractice/shop")

# Apply the static wait
time.sleep(5)

# store all products elements in an Element Array
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

expectedProduct = "iphone X"
# verify the product and click on add button for adding the product to the cart
for product in products:
    actualProduct = product.find_element(By.XPATH, "div/h4/a").text
    if actualProduct in expectedProduct:
        print("Product is : ", actualProduct)
        product.find_element(By.XPATH, "div/button").click()

# Apply the static wait
time.sleep(5)

# verify the cart
cartElement = driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']")
driver.execute_script("arguments[0].click();", cartElement)
time.sleep(5)
verifyProductCart = driver.find_elements(By.XPATH, "//div[@class='media-body']/h4/a")
for product in verifyProductCart:
    if product.text == expectedProduct:
        print("'", expectedProduct, "'", " is Successfully added to the cart...")
    else:
        print("'", expectedProduct, "'", " is not added to the cart successfully...")

# clicking on the checkOut Button
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(5)

# choosing the delivery location
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("india")
time.sleep(7)
driver.find_element(By.XPATH, "//div[@class='suggestions']//a[contains(.,'India')]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
time.sleep(5)

# clicking on purchase button
driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()

# verify that the product is successfully ordered or not
expectedMsg = "Success! Thank you! Your order will be delivered in next few weeks :-)."
actualMsg = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
if expectedMsg in actualMsg:
    print("'", expectedProduct, "'", " Product is Successfully Ordered...")
else:
    print("'", expectedProduct, "'", " Product is not Ordered successfully...")

# Apply the static wait
time.sleep(5)

# print a msg
print("Successfully Executed...")

# close the browser
driver.close()