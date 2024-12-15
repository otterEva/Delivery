from typing import List
from .coordinate import Coordinate
from .item import Item

class OrderedItem:
    def __init__(self, guid: str, quantity: int):
        self.guid = guid
        self.quantity = quantity

class DeliveryPoint:
    def __init__(self, coordinates: Coordinate, items: List[OrderedItem]):
        self.coordinates = coordinates
        self.items = items
