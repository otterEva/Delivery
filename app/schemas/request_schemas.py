from pydantic import BaseModel
from typing import List

class OrderedItemSchema(BaseModel):
    
    guid: str
    quantity: int

class DeliveryPointSchema(BaseModel):
    
    coordinates: List[float]  # [lat, lon]
    items: List[OrderedItemSchema]

class WarehouseSchema(BaseModel):
    
    coordinates: List[float] 
    items: List[str] 

class DeliveryRequestSchema(BaseModel):

    courier_start_point: List[float]
    delivery_points: List[DeliveryPointSchema]
    warehouses: List[WarehouseSchema]
    courier_capacity: int
