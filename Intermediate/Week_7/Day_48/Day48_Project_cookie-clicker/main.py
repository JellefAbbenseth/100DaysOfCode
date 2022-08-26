import time

from selenium import webdriver
from selenium.webdriver.common.by import By

DURATION = 0.1 * 60
DURATION_CHECK = 5

chrome_driver_path = "/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
store_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
for item in store_items:
    print(item.text)

# Todo: Check prices and money to buy the item every DURATION_CHECK

# start_time = time.time()
# print(start_time)
#
# while (start_time + DURATION) > time.time():
#     cookie.click()
#
# money = driver.find_element(By.ID, "money")
# print(f"Money: {money.text}")
# count_per_second = driver.find_element(By.ID, "cps")
# print(count_per_second.text)
#
# end_time = time.time()
# print(f"Dauer: {end_time - start_time}")

driver.quit()
