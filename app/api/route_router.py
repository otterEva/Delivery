from fastapi import APIRouter
from schemas.request_schemas import DeliveryRequestSchema
from schemas.response_schemas import RouteResponseSchema
from services.route_calculator import RouteCalculator
from services.maps_api import MapsAPI

router = APIRouter()

@router.post("/calculate_route", response_model=RouteResponseSchema)
def calculate_route(request: DeliveryRequestSchema):

    maps_api = MapsAPI()

    calculator = RouteCalculator(maps_api=maps_api)

    route = calculator.calculate_route(request)

    route_coords = [[stop.latitude, stop.longitude] for stop in route.stops]

    return RouteResponseSchema(route=route_coords, map_url=route.map_url)
