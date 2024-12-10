from pydantic import BaseModel
from typing import List

# —хема ответа на запрос построени€ маршрута
class RouteResponseSchema(BaseModel):
    # —писок координат маршрута, где кажда€ точка - это [широта, долгота]
    route: List[List[float]]
    # —сылка на карту маршрута
    map_url: str
