import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/-/de/dp/B08CF6PFZF/ref=sbl_dpx_kitchen-electric-cookware_B07V7GXSXJ_0"
goal_value = 165.00
headers = {
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 "
                  "Safari/537.36 "
}

response = requests.get(URL, headers=headers)
am_web_page = response.text

soup = BeautifulSoup(am_web_page, "html.parser")
article_price = soup.find(name="span", class_="a-offscreen")
article_titel = soup.find(name="span", id="productTitle")
price = float(article_price.getText().split("$")[0].replace(",", "."))
if price < goal_value:
    print("Amazon Price Alert!")
    print(article_price.getText())
    print(article_titel.getText())
    print(URL)
