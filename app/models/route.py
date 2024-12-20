from typing import List
from .coordinate import Coordinate


class Route:
    def __init__(self, stops: List[Coordinate], map_url: str):
        # ������ ��������� (stops), �������������� �������
        self.stops = stops
        # URL ����� �������� (map_url)
        self.map_url = map_url
