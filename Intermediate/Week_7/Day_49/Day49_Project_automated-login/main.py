from selenium import webdriver
from selenium.webdriver.common.by import By

USERNAME = "Test@Tester.com"
PASSWORD = "Tester"

chrome_driver_path = "/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/login/de?fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs"
           "&trk=guest_homepage-jobseeker_nav-header-signin")

username = driver.find_element(By.ID, "username")
username.send_keys(USERNAME)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
login = driver.find_element(By.CSS_SELECTOR, "#organic-div .btn__primary--large")
print(login.text)
