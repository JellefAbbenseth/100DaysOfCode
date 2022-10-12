# Data Entry Job Automation
# ToDo: update chrome_driver and check functionality
# registration and checking information and store it
# generate document and save it

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
