# Web browser automation using Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from time import sleep
service = Service(executable_path='/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/Automation-using-Python/Automation with Selenuim/chromedriver')

driver = webdriver.Chrome(service=service)
driver.get("https://google.com")

input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.send_keys("Selenium Documentation" + Keys.ENTER)
sleep(20)
# driver.quit()