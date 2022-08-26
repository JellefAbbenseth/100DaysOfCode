from selenium import webdriver
from selenium.webdriver.common.by import By

FIRST_NAME = "Test"
LAST_NAME = "Tester"
MAIL_ADDRESS = "Test@Tester.com"

chrome_driver_path = "/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")
form_first_name = driver.find_element(By.NAME, "fName")
form_first_name.send_keys(FIRST_NAME)
form_last_name = driver.find_element(By.NAME, "lName")
form_last_name.send_keys(LAST_NAME)
form_mail = driver.find_element(By.NAME, "email")
form_mail.send_keys(MAIL_ADDRESS)
sign_up = driver.find_element(By.TAG_NAME, "button")
sign_up.click()
