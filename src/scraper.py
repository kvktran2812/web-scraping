import numpy as np
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




#########################################
# Some soft test script below here

class MyScrapeUnit(ScrapeUnit):
    def __init__(self):
        self.data = "some data"

    def run(url):
        print(url)


my_scrape_unit = MyScrapeUnit()
my_scrape_unit.run()


scraper = Scraper("https://testing")
scraper.run()