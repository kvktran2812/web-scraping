from src.machine import *
from src.scraping import *

gmap = GoogleMapMachine()
gmap.scrape("Sushi Moto")

print(gmap.data)
