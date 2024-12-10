from fastapi import APIRouter
from schemas.request_schemas import DeliveryRequestSchema
from schemas.response_schemas import RouteResponseSchema
from services.route_calculator import RouteCalculator
from services.maps_api import MapsAPI

#Тут реализуется эндпоинт /calculate_route для расчёта маршрута

# Создаём маршрутизатор FastAPI для обработки запросов, связанных с маршрутами
router = APIRouter()

# Определяем эндпоинт для расчёта маршрута
@router.post("/calculate_route", response_model=RouteResponseSchema)
def calculate_route(request: DeliveryRequestSchema):
    #Обрабатывает запрос на построение маршрута

    # Создаём объект для работы с картографическим API 
    maps_api = MapsAPI()

    # Создаём объект для расчёта маршрута
    calculator = RouteCalculator(maps_api=maps_api)

    # Вызываем метод расчёта маршрута
    route = calculator.calculate_route(request)

     # Преобразуем маршрут в формат списка координат
    route_coords = [[stop.latitude, stop.longitude] for stop in route.stops]

     # Возвращаем результат с маршрутом и ссылкой на карту
    return RouteResponseSchema(route=route_coords, map_url=route.map_url)
