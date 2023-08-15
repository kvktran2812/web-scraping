from src.machine import *
import re

machine = GoogleMapMachine(name="Sushi Moto, Yonge Street, North York, ON")
machine.run()

print(machine.data)
