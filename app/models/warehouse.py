from typing import List
from .coordinate import Coordinate
from .item import Item

class Warehouse:
    def __init__(self, coordinates: Coordinate, available_items: List[Item]):
        self.coordinates = coordinates
        self.available_items = available_items
