from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Todo: Search fitting website
SPEED_TEST_URL = ""

chrome_driver_path = "/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(SPEED_TEST_URL)
sleep(2.0)
