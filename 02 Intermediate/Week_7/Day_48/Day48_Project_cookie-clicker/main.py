import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

DURATION = 1 * 60
DURATION_CHECK = 5

# chrome_driver_path = "/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
s = Service("/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe")
o = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=s, options=o)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

start_time = time.time()
time_seconds = time.time() + 10
cnt = 1
while True:
    cookie.click()
    if time.time() > time_seconds:
        prices = driver.find_elements(By.CSS_SELECTOR, "#store div b")
        price_data = []
        for i in range(8):
            price_data.append(int(prices[i].text.split()[-1].replace(",", "")))
        cookie_count = int(driver.find_element(By.ID, 'money').text.replace(',', ''))
        print(f"Money = {cookie_count}")
        for index in range(len(price_data) - 1, -1, -1):
            price = price_data[index]
            if cookie_count > price:
                store_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
                store_items[index].click()
                break
        time_seconds = time.time() + 10
        cnt += 1
    if (start_time + DURATION) < time.time():
        break

money = driver.find_element(By.ID, "money")
print(f"Money: {money.text}")
count_per_second = driver.find_element(By.ID, "cps")
print(count_per_second.text)

end_time = time.time()
print(f"Dauer: {end_time - start_time}")
print(cnt)

driver.quit()
