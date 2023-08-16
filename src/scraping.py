from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import networkx as nx


class Scraping:
    def __init__(self, driver=None):
        self.driver = driver
        self.soup = BeautifulSoup()
        self._graph = nx.MultiDiGraph()
        self._graph.add_node("Root")
        return

    def run(self):
        return

    def add_step(self, node_name, function, prev_step=None):
        self._graph.add_node(node_name)
        self._graph[node_name]['function'] = function

        if prev_step:
            self._graph.add_edge(prev_step, node_name)
        else:
            self._graph.add_edge("Root", node_name)


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
