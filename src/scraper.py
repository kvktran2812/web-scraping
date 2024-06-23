from bs4 import BeautifulSoup
import networkx as nx
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from abc import ABC, abstractmethod
import requests

class ScrapeUnit(ABC):
    def __init__(self):
        return
    
    @staticmethod
    @abstractmethod
    def run(url):
        return


class Scraper():
    def __init__(self, url):
        self.root = url
        return

    def run(self):
        return

class AutomaticScraper():
    def __init__(self, steps: int = 3, verbal=False) -> None:
        self.steps = steps
        self.verbal = verbal
        return
    
    def run(self, url):
        # print(url)
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            soup = BeautifulSoup(content, 'html.parser')

            print(f"SUCESS: {url}\nSTATUS CODE: {response.status_code}")

            links = soup.find_all("a")
            links = [link.text for link in links]
            print(len(links))
        else:
            print(f"ERROR: Failed to request {url}\n\
                  Status code: {response.status_code}")
        return


#########################################
# Some soft test script below here

# class MyScrapeUnit(ScrapeUnit):
#     def __init__(self):
#         self.data = "some data"

#     @staticmethod
#     def run(url):
#         print(url)


# my_scrape_unit = MyScrapeUnit()
# my_scrape_unit.run("https://testing")


# scraper = Scraper("https://testing")
# scraper.run()


### 
automatic = AutomaticScraper()
automatic.run("https://news.google.com/home?hl=en-US&gl=US&ceid=US:en")