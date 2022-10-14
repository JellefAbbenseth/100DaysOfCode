# Data Entry Job Automation
# ToDo: update chrome_driver and check functionality
# registration and checking information and store it
# generate document and save it

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

SITE_URL = ""

chrome_driver_path = "/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(SITE_URL)
sleep(5.0)
