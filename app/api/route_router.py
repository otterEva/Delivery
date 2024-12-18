from fastapi import APIRouter, HTTPException, status
from app.schemas.request_schemas import DeliveryRequestSchema
from app.services.gis_request import RequestService
from app.services.gis_responce import ResponceService
from app.exceptions import GisException, JsonDecodeException, BaseAppException, CreateGisRequestException, CheckStatusException
router = APIRouter()

@router.post("/calculate_route")
async def calculate_route(delivery_request: DeliveryRequestSchema):

	try:
		ready_request = RequestService.prepare_request(delivery_request)
		ready_responce = await ResponceService.get_2gis_responce(ready_request)
	except GisException:
		raise HTTPException(status_code = status.HTTP_406_NOT_ACCEPTABLE, detail = '2gis умер')
	except JsonDecodeException:
		raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)
	except BaseAppException as e:
		raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = str(e))
	except Exception:
		raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)
	except CreateGisRequestException:
		raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)
	except CheckStatusException:
		raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)
	return ready_responce
