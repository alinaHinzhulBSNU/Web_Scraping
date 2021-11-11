# TASK: Get list of articles (habr.com)

import requests
from bs4 import BeautifulSoup as BS

page_number = 1
count = 1

while True:
    # Get page
    page = requests.get("https://habr.com/ru/all/page" + str(page_number) + "/")
    html = BS(page.content, 'html.parser')

    # Articles from page
    articles = html.select(".tm-articles-list__item")

    if len(articles):  # If page is not empty
        for article in articles:
            # Title
            title = article.select(".tm-article-snippet > .tm-article-snippet__title > "
                                   ".tm-article-snippet__title-link span")
            # Views
            views = article.select(".tm-data-icons > .tm-icon-counter > .tm-icon-counter__value")
            if title and views:
                print("№" + str(count) + " - " + title[0].text + " (" + views[0].text + " views)")
                count += 1
        page_number += 1
    else:
        break
