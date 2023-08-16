from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re


def standard_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=es")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    m_driver = webdriver.Chrome(options=options)
    return m_driver


class GoogleMapMachine:
    def __init__(self, name, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = standard_driver()

        self.name = name
        self.elements = {}
        self.steps = []
        self.data = {}

    def _setup_resource(self):
        self.driver.get("https://www.google.com/maps")
        self.elements['search_input'] = '//*[@id="searchboxinput"]'
        elem = self.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
        elem.send_keys("Sushi Moto, Yonge Street, Toronto, ON")
        elem.send_keys(Keys.ENTER)
        time.sleep(2)
        return

    def get_general_info(self):
        info_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div'
        info = self.driver.find_element(By.XPATH, info_xpath)
        html = info.get_attribute("innerHTML")

        soup = BeautifulSoup(html, 'lxml')

        # get total reviews and star
        total_reviews_div = soup.find("div", {"class": "F7nice"})
        total_star = total_reviews_div.span.get_text()
        number_of_review = total_reviews_div.span.next_sibling.span.get_text()
        number_of_review = re.findall(r'\d+,\d+', number_of_review)
        number_of_review = number_of_review[0].replace(',', '')

        self.data["result"] = {
            'total_star': float(total_star),
            'number_of_review': int(number_of_review),
            'reviews': [],
        }

    def run(self):
        self._setup_resource()
        self.get_general_info()


class ScrapeStep:
    def __init__(self, driver):
        self.driver = driver
        return

    def run(self):
        return
