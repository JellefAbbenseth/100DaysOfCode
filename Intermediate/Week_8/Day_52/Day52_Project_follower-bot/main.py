from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

ECOSIA_URL = "https://duckduckgo.com/"

search_term = input("Please type in what you want to search: ")

chrome_driver_path = "/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(ECOSIA_URL)
sleep(2.0)

search_field = driver.find_element(
    By.CSS_SELECTOR,
    "#search_form_input_homepage"
)
search_field.send_keys(search_term)


send_search = driver.find_element(
    By.CSS_SELECTOR,
    "#search_button_homepage"
)
send_search.click()

# Todo: Check for wiki entry
# check if there are search entries

check_entries = driver.find_elements(
    By.CSS_SELECTOR,
    "" # get entries
)
