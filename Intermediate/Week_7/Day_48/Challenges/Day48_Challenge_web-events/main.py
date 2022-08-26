from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/Jellef/Documents/Programme/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
upcoming_event_names = driver.find_elements(
    By.CSS_SELECTOR, '.event-widget .shrubbery .menu li a'
)
upcoming_event_dates = driver.find_elements(
    By.CSS_SELECTOR, '.event-widget .shrubbery .menu li time'
)
events = dict()
for i in range(len(upcoming_event_dates) - 1):
    events.update({i: {'time': upcoming_event_dates[i].text, 'name': upcoming_event_names[i].text}})

print(events)

driver.quit()
