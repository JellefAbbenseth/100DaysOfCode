from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


SPEED_TEST_URL = "https://www.speedtest.net/"

chrome_driver_path = "/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(SPEED_TEST_URL)
sleep(2.0)

more_options_privacy = driver.find_element(By.CSS_SELECTOR, "#onetrust-pc-btn-handler")
more_options_privacy.click()
sleep(2.0)


confirm_choice_privacy = driver.find_element(
    By.CSS_SELECTOR,
    "#onetrust-consent-sdk .ot-pc-footer button"
)
confirm_choice_privacy.click()

# Todo: Start Speedtest
