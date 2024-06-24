from bs4 import BeautifulSoup
import networkx as nx
from abc import ABC, abstractmethod
import requests
import matplotlib.pyplot as plt
from scraper import default_filter_v1, default_filter_v2



class LinkMap():
    def __init__(self, depth=1, filter_function=default_filter_v2) -> None:
        # parameters
        self.depth = depth
        self.filter_function = filter_function
        self.graph = nx.Graph()
        self.track_url = list()
    

    def run(self, url):
        self.graph.add_node(url)
        scrape_list = [url]
        count = 0

        while count != self.depth:
            for url in scrape_list:
                links = self.get_all_links(url, self.filter_function)
            count += 1


    @staticmethod
    def get_all_links(url, filter_function):
        links = None
        try:
            response = requests.get(url)
            if response.status_code == 200:
                content = response.text
                soup = BeautifulSoup(content, "html.parser")

                links = soup.find_all("a")
                links = list(filter(filter_function, links))
            else:
                print(f"ERROR: Failed to request {url}\n\
                Status code: {response.status_code}")
        except Exception as e:
            print(e)
            print(f"ERROR: Can't request {url}, will not add this url to the graph structure")
        return links


linkmap = LinkMap()
links = linkmap.get_all_links("https://news.google.com/home?hl=en-US&gl=US&ceid=US:en", default_filter_v2)