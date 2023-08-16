from src.machine import *
import re
import networkx as nx
import matplotlib.pyplot as plt
from src.scraping import Scraping


def func():
    print("hello")


driver = standard_driver()

scraping = Scraping(driver)
scraping.add_step(1, func)
scraping.add_step(2, func)
scraping.add_step(3, func, 1)
scraping.run()
