from bs4 import BeautifulSoup
import networkx as nx
from abc import ABC, abstractmethod
import requests
import matplotlib.pyplot as plt



class LinkMap():
    def __init__(self, depth=1, filter_function=None) -> None:
        self.depth = depth
        self.filter_function = filter_function
        self.graph = nx.Graph()
        return
    
    def run(self, url):
        response = requests.get(url=url)
        if response.status_code == 200:
            content = response.text
            soup = BeautifulSoup(content, "html.parser")

            self.graph.add_node(url)
        else:
            print(f"ERROR: Failed to request {url}\n\
                  Status code: {response.status_code}")
        return
    

linkmap = LinkMap()
linkmap.run("https://news.google.com/home?hl=en-US&gl=US&ceid=US:en")

nx.draw(linkmap.graph)
plt.show()