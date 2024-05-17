# Web browser automation using Selenium
'''
Selenium is one of the popular open source used tool used for test automation.
Testing is reffered to web applications
Selenium have lot of tools each with its specific functions
'''
from selenium import webdriver 
# Selenium WebDriver is a tool used for automating web application testing to verify that it performs expectedly. You can simulate user actions like clicking, typing, and navigating web pages.
from selenium.webdriver.chrome.service import Service
# The Service class is used to manage the starting and stopping of the WebDriver executable. This is useful when you need more control over the WebDriver service, such as setting custom paths or environment variables.
from selenium.webdriver.common.by import By
# The By class provides a mechanism to locate elements within a document. It is used to locate elements by various strategies like ID, name, XPath, CSS selector, etc.
from selenium.webdriver.common.keys import Keys #Optional
from selenium.webdriver.support.ui import WebDriverWait  #optional
from selenium.webdriver.support import expected_conditions as EC #optional
from colorama import init, Fore, Style # for printing colored text
# Colorama is a library that makes it easier to print colored text in the terminal. It is cross-platform, so it works on Windows, Linux, and Mac.
import os
from time import sleep


# BASICS TO setup selenium
service = Service(executable_path='/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/Automation-using-Python/Automation with Selenuim/chromedriver')
driver = webdriver.Chrome(service=service)
# driver.get("https://www.saucedemo.com/v1/")
'''
driver.get("https://google.com")

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)
input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
# input_element.clear()  #to clear if anything is there

# input_element.send_keys("python.org")
input_element.send_keys("python.org" + Keys.ENTER)

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"python.org"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT,"python.org")
link.click()
# to make the element exists
sleep(10)
# driver.quit()
'''

def print_colored(text, color):
    colors = {"red": Fore.RED, "green": Fore.GREEN, "reset": Style.RESET_ALL}
    print(colors[color] + text + colors["reset"])

try:
    # Test 1: Open the website
    driver.get("https://www.saucedemo.cm/v1/")
    print_colored("Test 1 Passed: The title of the website is " + driver.title, "green")
except Exception as e:
    print_colored("Test 1 Failed: " + str(e), "red")

sleep(10)
