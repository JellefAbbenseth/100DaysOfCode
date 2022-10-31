from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


PEXELS_SITE_URL = "https://500px.com/popular"
N_TIMES = 3

chrome_driver_path = "/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get(PEXELS_SITE_URL)
sleep(5.0)

first_picture = driver.find_element(
    By.CSS_SELECTOR,
    "#justifiedGrid div"
)
print(first_picture.tag_name)
first_picture.click()

for i in range(N_TIMES):
    sleep(5.0)
    next_button = driver.find_element(
        By.CSS_SELECTOR,
        ".Elements__ModalContainer-olfmpd-2 .ecpwQD"
    )
    next_button.click()
print("finished")
