from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

ECOSIA_URL = "https://www.ecosia.org/?c=de"

search_term = input("Please type in what you want to search: ")

chrome_driver_path = "/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(ECOSIA_URL)
sleep(2.0)

search_field = driver.find_element(
    By.CSS_SELECTOR,
    "#__layout .search-form__input-wrapper input"
)
search_field.send_keys(search_term)

# Todo: check send_search (Check for submit in Form)

send_search = driver.find_element(
    By.CSS_SELECTOR,
    " "  # form
)
search_field.submit()
