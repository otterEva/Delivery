from pydantic import BaseModel
from typing import Tuple, Dict, List

class Courier(BaseModel):
    courier_id: int
    address: Tuple[float, float]

class SubOrder(BaseModel):
    address: Tuple[float, float]
    items: Dict[int, int]

class OrderData(BaseModel):
    address: Tuple[float, float]

class Order(BaseModel):
    order: OrderData
    suborders: List[SubOrder]

class DeliveryRequestSchema(BaseModel):
    couriers: List[Courier]
    orders: List[Order]