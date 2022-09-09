from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Todo: Search fitting website
ECOSIA_URL = "https://www.ecosia.org/?c=de"

chrome_driver_path = "/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(ECOSIA_URL)
sleep(2.0)

search_field = driver.find_element(
    By.CSS_SELECTOR,
    "#__layout .search-form__input-wrapper input"
)
search_field.send_keys("Test")

send_search = driver.find_element(
    By.CSS_SELECTOR,
    "#__layout .search-form-search-field .search-form__submit"
)
send_search.click()
