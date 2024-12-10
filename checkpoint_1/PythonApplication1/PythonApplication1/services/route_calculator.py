from models.coordinate import Coordinate
from models.route import Route
from schemas.request_schemas import DeliveryRequestSchema
from .maps_api import MapsAPI

#Строится маршрут: склад ? точка доставки ? возвращение в начальную точку

class RouteCalculator:
    def __init__(self, maps_api: MapsAPI):
        self.maps_api = maps_api

    def calculate_route(self, request: DeliveryRequestSchema) -> Route:

        #получение начальной точки курьера
        start = Coordinate(*request.courier_start_point)

        #получение координат склада
        warehouse_coords = request.warehouses[0].coordinates if request.warehouses else request.courier_start_point

        #получение координат точки доставки
        delivery_coords = request.delivery_points[0].coordinates if request.delivery_points else request.courier_start_point

        #формирование списка остановок
        stops = [
            Coordinate(*warehouse_coords),
            Coordinate(*delivery_coords),
            start
        ]

        #создание объекта маршрута
        return Route(stops=stops, map_url="http://example.com/map")
