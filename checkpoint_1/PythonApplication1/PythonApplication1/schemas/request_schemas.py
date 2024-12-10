from pydantic import BaseModel
from typing import List

# Описание товара в заказе
class OrderedItemSchema(BaseModel):
    #Уникальный идентификатор товара
    guid: str
    #Количество единиц товара в заказе
    quantity: int

# Описание точки доставки
class DeliveryPointSchema(BaseModel):
    # Координаты точки доставки в формате [широта, долгота]
    coordinates: List[float]  # [lat, lon]
    # Список товаров, которые нужно доставить в эту точку
    items: List[OrderedItemSchema]

# Описание склада
class WarehouseSchema(BaseModel):
    #Координаты склада в формате [широта, долгота]
    coordinates: List[float] 
    #Список уникальных идентификаторов товаров, доступных на складе
    items: List[str] 

# Описание данных запроса на построение маршрута
class DeliveryRequestSchema(BaseModel):
    # Координаты начальной точки курьера в формате [широта, долгота]
    courier_start_point: List[float]
    # Список точек доставки
    delivery_points: List[DeliveryPointSchema]
    # Список складов
    warehouses: List[WarehouseSchema]
    # Максимальная грузоподъёмность курьера (в условных единицах)
    courier_capacity: int
