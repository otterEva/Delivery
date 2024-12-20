from pydantic import BaseModel
from typing import Tuple, Dict, List, Optional


class Courier(BaseModel):
    courier_id: int
    address: Tuple[float, float]
    duration: Optional[Dict[int,float]] = {}
    distance: Optional[Dict[int,float]] = {}



class SubOrder(BaseModel):
    address: Tuple[float, float]
    items: Dict[int, int]
    duration: Optional[Dict[int,float]] = {}
    distance: Optional[Dict[int,float]] = {}

class OrderData(BaseModel):
    address: Tuple[float, float]
    duration: Optional[Dict[int,float]] = {}
    distance: Optional[Dict[int,float]] = {}


class Order(BaseModel):
    order: OrderData
    suborders: List[SubOrder]


class DeliveryRequestSchema(BaseModel):
    couriers: List[Courier]
    orders: List[Order]
