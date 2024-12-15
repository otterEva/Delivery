from pydantic import BaseModel
from typing import Tuple, Dict, List, Optional
    
class Courier(BaseModel):
    courier_id: int
    max_capacity: Optional[int] = None
    max_mass: Optional[int] = None
    courier_address: Tuple[float, float]

class SubOrder(BaseModel):
    warehouse_address: Tuple[float, float]
    items: Dict[int, int] 

class Order(BaseModel):
    delivery_address: Tuple[float, float]
    suborders: List[SubOrder]

class DeliveryRequestSchema(BaseModel):
    couriers: List[Courier]
    orders: List[Order]