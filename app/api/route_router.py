from fastapi import APIRouter
from app.schemas.request_schemas import DeliveryRequestSchema
from app.services.gis_request import RequestService
from app.services.gis_responce import ResponceService
from app.services.manage_data import DataManageService
router = APIRouter()

@router.post("/calculate_route")
async def calculate_route(delivery_request: DeliveryRequestSchema):

	ready_request, dataholder = RequestService.prepare_request(delivery_request)
	#ready_responce = await ResponceService.gather_2gis_list_responce(ready_request)
	#updated_dataholder = DataManageService.update_dataholder(dataholder, ready_responce)
	return ready_request
