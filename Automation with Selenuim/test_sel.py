# Web browser automation using Selenium
'''
Selenium is one of the popular open source used tool used for test automation.
Testing is reffered to web applications
Selenium have lot of tools each with its specific functions
'''
from selenium import webdriver 
# Selenium WebDriver is a tool used for automating web application testing to verify that it performs expectedly. 
# also to control our web browser
# You can simulate user actions like clicking, typing, and navigating web pages.
# https://googlechromelabs.github.io/chrome-for-testing/
from selenium.webdriver.chrome.service import Service
# The Service class is used to manage the starting and stopping of the WebDriver executable. This is useful when you need more control over the WebDriver service, such as setting custom paths or environment variables.
from selenium.webdriver.common.by import By
# The By class provides a mechanism to locate elements within a document. It is used to locate elements by various strategies like ID, name, XPath, CSS selector, etc.
from selenium.webdriver.common.keys import Keys #Optional
from selenium.webdriver.support.ui import WebDriverWait  #optional
from selenium.webdriver.support import expected_conditions as EC #optional
from colorama import Fore, Style # for printing colored text
# Colorama is a library that makes it easier to print colored text in the terminal. It is cross-platform, so it works on Windows, Linux, and Mac.

# BASICS TO setup selenium
import os
from pathlib import Path
os.chdir(os.path.dirname(__file__))
# print(os.getcwd())
wait_load = webdriver.ChromeOptions()
wait_load.add_experimental_option("detach",True)

web_service = Service(executable_path='/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/Automation-using-Python/Automation with Selenuim/chromedriver')

driver = webdriver.Chrome(service=web_service,options=wait_load)
driver.get("https://google.com")
# sleep(10)

WebDriverWait(driver,2).until(
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)
input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.send_keys("python.org",Keys.ENTER)
# driver.quit()



username = "standard_user"
password = "secret_sauce"

input_element = driver.find_element(By.ID,"user-name")
password_element = driver.find_element(By.ID,"password")
login_element = driver.find_element(By.ID,"login-button")

input_element.send_keys(username)
password_element.send_keys(password)
login_element.click()


# items = driver.find_elements(By.CLASS_NAME,"inventory_item")
# #return type: list of WebElement Full name:
# # print("Iteams are:",items.text)
# for item in items:
#     each_item = item.find_element(By.CLASS_NAME,"inventory_item_name").text
#     # print(each_item)
#     if 'T_shirt' in each_item:
#         add_to_cart_button = item.find_element(By.CLASS_NAME, "btn_primary btn_inventory")
#         add_to_cart_button.click()
#         # botton.click()
#     # print((each_item))
# sleep(30)

items = driver.find_elements(By.CLASS_NAME, 'inventory_item')
# print("Items available are: ")


for item in items:
    item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
    # print(item_name)
    if "T-Shirt" in item_name:
        # #inventory_container > div > div:nth-child(3) > div.pricebar > button
        # since nth-child(3) depends on the div we select, we don't want that
        # As we want to find the same "add to cart" button in every div despite the child number for the div list
        # we remove the nth-child(3) and use it
        add_to_cart_button = item.find_element(By.CSS_SELECTOR, "#inventory_container > div > div > div.pricebar > button")
        add_to_cart_button.click()

# Go to Cart
cart_button = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
cart_button.click()
'''
Different locator strategies (CLASS_NAME, CSS_SELECTOR, XPATH,TAG_NAME) are chosen based on what is most effective and readable for the specific element being targeted. This flexibility allows you to handle a wide variety of HTML structures and ensures that your Selenium script is both robust and maintainable. '''

checkout_button = driver.find_element(By.CSS_SELECTOR,'#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button')
checkout_button.click()
input_fields = driver.find_elements(By.TAG_NAME, "input")
input_data = ["John", "Doe", "123124"]
sleep(0.5)
for input_field, input_data in zip(input_fields,input_data):
    input_field.send_keys(input_data)
    sleep(2)

input_fields[-1].click() # or find the continue element and click it
sleep(1)

# Finish Checkout
# btn_action cart_button -> should be used as btn_action.cart_button


# Define an explicit wait with a timeout of 10 seconds
wait = WebDriverWait(driver, 10)

# Locate the finish button element using a CSS selector
finish_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_action.cart_button")))

sleep(1)
# Click the finish button
finish_button.click()
sleep(30)

#Excercise : Remove item that cost more than n dollars:let n = $20

# for iteam in iteams:
#     iteam_name = driver.find_element(By.CLASS_NAME,"inventory_item")
#     print()

# def print_colored(text, color):
#     colors = {"red": Fore.RED, "green": Fore.GREEN, "reset": Style.RESET_ALL}
#     print(colors[color] + text + colors["reset"])

# try:
#     # Test 1: Open the website
#     driver.get("https://www.saucedeo.cm/v1/")
#     print_colored("Test 1 Passed: The title of the website is " + driver.title, "green")
# except Exception as e:
#     print_colored("Test 1 Failed: " + str(e), "red")

# sleep(10)
