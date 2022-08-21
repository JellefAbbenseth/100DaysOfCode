import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/")
bm_web_page = response.text

soup = BeautifulSoup(bm_web_page, "html.parser")
article_titles = [article.getText() for article in soup.select(".article-title-description__text .title")]

with open("Top-100-movies.txt", "w", encoding="utf-8") as file:
    for title in article_titles[::-1]:
        file.writelines(title + "\r")
