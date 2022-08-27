import time

from selenium import webdriver
from selenium.webdriver.common.by import By

DURATION = 0.5 * 60
DURATION_CHECK = 5

chrome_driver_path = "/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
store_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
prices = driver.find_elements(By.CSS_SELECTOR, "#store div b")
price_data = []
for i in range(8):
    price_data.append(prices[i].text.split()[-1])
    # print(store_items[i].text)


# print(price_data)


# Todo: check code -> money is nearly zero every turn

def buy_item():
    global price_data, store_items
    money_element = driver.find_element(By.ID, "money")
    num_cookies = int(money_element.text)
    print(f"Money = {num_cookies}")
    for index in range(len(price_data) - 1):
        if num_cookies < int(price_data[index]) and index > 0:
            store_items[index].click()
            return


start_time = time.time()
cnt = 1
while True:
    if (start_time + DURATION) > (start_time + (cnt * DURATION_CHECK)):
        buy_item()
        print(f"Counter: {cnt}")
        cnt += 1
    cookie.click()
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
