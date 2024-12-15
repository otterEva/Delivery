from fastapi import APIRouter
from app.schemas.request_schemas import DeliveryRequestSchema
from app.services.maps_api import get_distances_and_durations, get_permutations
router = APIRouter()

@router.post("/calculate_route")
def calculate_route(data: DeliveryRequestSchema):

	got_coorinates_and_objects = get_distances_and_durations(data)
	got_coordinates_only = [coordinate[0] for coordinate in got_coorinates_and_objects]

	perms = get_permutations(got_coordinates_only)
	return perms
