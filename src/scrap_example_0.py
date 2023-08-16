from src.machine import *
import re
import networkx as nx
import matplotlib.pyplot as plt
from src.scraping import *

machine = GoogleMapMachine("Sushi Moto")
machine.run()

print(machine.data)
