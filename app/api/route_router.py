from fastapi import APIRouter
from app.schemas.request_schemas import DeliveryRequestSchema
from app.services.gis_request import RequestService
from app.services.gis_responce import ResponceService
from app.services.manage_data import DataManageService
from starlette.responses import Response
from starlette.status import HTTP_404_NOT_FOUND, HTTP_409_CONFLICT, HTTP_201_CREATED
import structlog

logger = structlog.get_logger()
router = APIRouter()


@router.post("/calculate_route")
async def calculate_route(delivery_request: DeliveryRequestSchema):
    try:
        ready_request, dataholder = RequestService.prepare_request(delivery_request)
        ready_responce = await ResponceService.gather_2gis_list_responce(ready_request)
        updated_dataholder = DataManageService.update_dataholder(
            dataholder, ready_responce
        )
    except:
        logger.error("Something went wrong at the API side")
        return Response(status_code=HTTP_409_CONFLICT)
    return updated_dataholder
