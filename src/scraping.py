import time
from bs4 import BeautifulSoup
import re
import networkx as nx
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver


def setup_scrape_google_map(driver, soup, name=""):
    driver.get("https://www.google.com/maps")
    xpath = '//*[@id="searchboxinput"]'
    elem = driver.find_element(By.XPATH, xpath)
    elem.send_keys("Sushi Moto, Yonge Street, Toronto, ON")
    elem.send_keys(Keys.ENTER)
    time.sleep(2)
    return


def get_general_info(driver, soup):
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


class Scraping:
    def __init__(self, driver=None):
        self.driver = driver
        self.soup = BeautifulSoup()
        self._graph = nx.MultiDiGraph()
        self._graph.add_node("Root")
        self.data = {}
        return

    def run(self):
        # Get next nodes from Root node
        edges = self._graph.out_edges("Root")
        next_nodes = [edge[1] for edge in edges]

        while next_nodes:
            current_nodes = next_nodes
            next_nodes = []
            for node in current_nodes:
                # Run the current node and save data
                node_data = self._graph.nodes[node]
                function = node_data["function"]
                inputs = node_data["inputs"]
                output = function(self.driver, self.soup, *inputs)
                self.save_data(output)

                # Get to next node
                edges = self._graph.out_edges(node)
                [next_nodes.append(edge[-1]) for edge in edges]
        return

    def add_step(self, node_name, function, inputs, prev_step=None):
        self._graph.add_node(node_name)
        self._graph.nodes[node_name]['function'] = function
        self._graph.nodes[node_name]['inputs'] = inputs

        if prev_step:
            self._graph.add_edge(prev_step, node_name)
        else:
            self._graph.add_edge("Root", node_name)

    def save_data(self, data):
        if data:
            for d in data:
                value = data[d]
                self.data[d] = value

    def _validate_function(self):
        return


class Step:
    def __init__(self, soup, driver):
        self.soup = soup
        self.driver = driver
        self.next = {}
        return

    def _validate_inputs(self):
        return True

    def run(self):
        return
