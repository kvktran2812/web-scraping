from src.machine import *
import re
import networkx as nx
import matplotlib.pyplot as plt


def func1():
    print("Hello World")


graph = nx.MultiDiGraph()
graph.add_node("New York")
graph.add_node("Tokyo")
graph.add_node("London")
graph.add_node("Dehli")
graph.add_edge("New York", "Tokyo")
graph.add_edge("New York", "Dehli")
graph.add_edge("Tokyo", "London")

London = graph.nodes["London"]
London["function"] = func1
print(London)

print(graph.out_edges("New York"))
