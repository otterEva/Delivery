from models.coordinate import Coordinate
from models.route import Route
from schemas.request_schemas import DeliveryRequestSchema
from .maps_api import MapsAPI


class RouteCalculator:
    def __init__(self, maps_api: MapsAPI):
        self.maps_api = maps_api

    def calculate_route(self, request: DeliveryRequestSchema) -> Route:
        start = Coordinate(*request.courier_start_point)

        warehouse_coords = (
            request.warehouses[0].coordinates
            if request.warehouses
            else request.courier_start_point
        )

        delivery_coords = (
            request.delivery_points[0].coordinates
            if request.delivery_points
            else request.courier_start_point
        )

        stops = [Coordinate(*warehouse_coords), Coordinate(*delivery_coords), start]

        return Route(stops=stops, map_url="http://example.com/map")
