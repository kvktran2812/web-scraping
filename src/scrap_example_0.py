from src.machine import *
from src.scraping import *
from src.google_news import *
from bs4 import BeautifulSoup


def get_info(article):
    print(article.prettify())
    news_provider = article.article.div.div.a.get_text()
    news_title = article.h3.a.get_text()
    news_time = article.time
    news_datetime = news_time["datetime"]
    news_time_text = news_time.get_text()
    news_link = article.article.a["href"]

    data = {
        "provider": news_provider,
        "title": news_title,
        "datetime": news_datetime,
        "timetext": news_time_text,
        "link": news_link,
    }

    return data


news = GoogleNews()
data = news.search("inflation")
print(news.tab)
