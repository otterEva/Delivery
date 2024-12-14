from pydantic import BaseModel
from typing import List

class RouteResponseSchema(BaseModel):
    
    route: List[List[float]]
    map_url: str
