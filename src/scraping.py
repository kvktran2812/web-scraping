import time
from bs4 import BeautifulSoup
import re
import networkx as nx
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver


def setup_scrape_google_map(driver, name=""):
    driver.get("https://www.google.com/maps")
    xpath = '//*[@id="searchboxinput"]'
    elem = driver.find_element(By.XPATH, xpath)
    elem.send_keys("Sushi Moto, Yonge Street, Toronto, ON")
    elem.send_keys(Keys.ENTER)
    time.sleep(2)
    return


def get_general_info(driver):
    info_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div'
    info = driver.find_element(By.XPATH, info_xpath)
    html = info.get_attribute("innerHTML")
    soup = BeautifulSoup(html, "lxml")

    # get total reviews and star
    total_reviews_div = soup.find("div", {"class": "F7nice"})
    total_star = total_reviews_div.span.get_text()
    number_of_review = total_reviews_div.span.next_sibling.span.get_text()
    number_of_review = re.findall(r'\d+,\d+', number_of_review)
    number_of_review = number_of_review[0].replace(',', '')

    return {
        'total_star': float(total_star),
        'number_of_review': number_of_review,
        'reviews': [],
    }

