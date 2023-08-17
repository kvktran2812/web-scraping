from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
from selenium.webdriver.support import expected_conditions as EC


def standard_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=es")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    m_driver = webdriver.Chrome(options=options)
    return m_driver


class GoogleMapMachine:
    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = standard_driver()
        self.elements = {}
        self.steps = []
        self.data = {}

    def _setup_resource(self, name):
        self.driver.get("https://www.google.com/maps")
        self.elements['search_input'] = '//*[@id="searchboxinput"]'
        elem = self.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
        elem.send_keys(name)
        elem.send_keys(Keys.ENTER)
        time.sleep(1.5)

    def _get_general_info(self):
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
        time.sleep(1.5)

    def _go_to_reviews_section(self):
        reviews_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]'
        reviews_button = self.driver.find_element(By.XPATH, reviews_xpath)
        reviews_button.send_keys(Keys.ENTER)
        time.sleep(1.5)

        elem = self.driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
        html = elem.get_attribute("innerHTML")

        # page_source = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        print(soup.prettify())

    def scrape(self, name):
        self._setup_resource(name)
        self._get_general_info()
        self._go_to_reviews_section()
