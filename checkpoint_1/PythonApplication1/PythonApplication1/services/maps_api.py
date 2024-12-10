from typing import List
from models.coordinate import Coordinate

class MapsAPI:
    def get_route_data(self, origin: Coordinate, destinations: List[Coordinate]):
        # Заглушка. Симулируем запрос к картам.
        return {"distances": {}, "durations": {}}
