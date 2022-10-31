from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

USERNAME = "Test@Tester.com"
PASSWORD = "Tester"
NUMBER_SAVE = 10

chrome_driver_path = "/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/login/de?fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs"
           "&trk=guest_homepage-jobseeker_nav-header-signin")

privacy_buttons = driver.find_elements(By.CSS_SELECTOR, "#artdeco-global-alert-container button")
print(privacy_buttons[1].text)
privacy_buttons[1].click()

username = driver.find_element(By.ID, "username")
username.send_keys(USERNAME)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
login = driver.find_element(By.CSS_SELECTOR, "#organic-div .btn__primary--large")
print(login.text)

input("Continue?! ")

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
sleep(2.0)
job_search_results = driver.find_elements(By.CSS_SELECTOR, "#main .jobs-search-results-list ul li")
print(len(job_search_results))

job_name = []

for index in range(NUMBER_SAVE):
    job_search_results[index].click()
    sleep(1)
    job_name.append(driver.find_element(
        By.CSS_SELECTOR,
        "#main .job-view-layout h2"
    ))
    job_save = driver.find_element(
        By.CSS_SELECTOR,
        "#main .jobs-save-button"
    )
    # job_save.click()
    print(f"Job Name: {job_name[index].text}")
    print(f"Job saved: {job_save.text}")

