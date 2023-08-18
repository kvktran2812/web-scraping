import time
from bs4 import BeautifulSoup
import re
import networkx as nx
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from src.machine import *


class GoogleNews:
    def __init__(self):
        self.driver = standard_driver()
        self.tab = {}
        self.data = {}
        self.elem = {}
        self._setup()

    def _setup(self):
        # Setup search elem
        self.driver.get("https://news.google.com/home?hl=en-CA&gl=CA&ceid=CA:en")
        search_xpath = '//*[@id="gb"]/div[2]/div[2]/div[2]/form/div[1]/div/div/div/div/div[1]/input[2]'
        self.elem["search"] = self.driver.find_element(By.XPATH, search_xpath)

        # Setup tabs
        header = self.driver.find_element(By.TAG_NAME, "header")
        self.elem["header"] = header
        soup = BeautifulSoup(header.get_attribute("innerHTML"), 'lxml')
        header_tab = soup.find("div", {"class": "gb_pd gb_cd"})
        tabs = header_tab.find_all("a")
        for t in tabs:
            if t.has_attr("href"):
                name = t.get_text()
                self.tab[name] = t["href"]

    @staticmethod
    def _get_article_info(article):
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

    def search(self, title):
        search_elem = self.elem["search"]
        search_elem.send_keys(title)
        search_elem.send_keys(Keys.ENTER)
        time.sleep(1)

        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        articles = soup.find_all('div', {"class": "xrnccd"})
        data = [self._get_article_info(a) for a in articles]
        return data
