from fastapi import APIRouter
from app.schemas.request_schemas import DeliveryRequestSchema
from app.services.gis_request import RequestService
from app.services.gis_responce import ResponceService
router = APIRouter()

@router.post("/calculate_route")
async def calculate_route(delivery_request: DeliveryRequestSchema):

	ready_request = RequestService.prepare_request(delivery_request)
	ready_responce = await ResponceService.gather_2gis_list_responce(ready_request)
	return ready_responce
