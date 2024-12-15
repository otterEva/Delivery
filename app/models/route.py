from typing import List
from .coordinate import Coordinate

class Route:
    def __init__(self, stops: List[Coordinate], map_url: str):
        #—писок координат (stops), представл€ющих маршрут
        self.stops = stops
        #URL карты маршрута (map_url)
        self.map_url = map_url
