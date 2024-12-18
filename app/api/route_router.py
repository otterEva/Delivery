from fastapi import APIRouter
from app.schemas.request_schemas import DeliveryRequestSchema
from app.services.gis_request import RequestService
import httpx
import time
import json

router = APIRouter()

@router.post("/calculate_route")
def calculate_route(delivery_request: DeliveryRequestSchema):

	headers = {"Content-Type": "application/json"}
	api_key = "d7d625b0-6754-4633-8ad0-107de6cecc40"

	ready_request = RequestService.prepare_request(delivery_request)
	return ready_request

	
	# task_id = httpx.post(url = f"https://routing.api.2gis.com/async_matrix/create_task/get_dist_matrix?key={api_key}&version=2.0",
	# 									headers = headers, json=data).json()
	
	# while True:
	# 	task_status = httpx.get(url = f'https://routing.api.2gis.com/async_matrix/result/get_dist_matrix/{task_id["task_id"]}?key={api_key}',
	# 										headers = headers).json()
	

	# 	if task_status["status"] == 'TASK_CANCELED':
	# 		return "задача отменена"
	# 	if task_status["status"] == 'TASK_IN_QUEUE' or 'TASK_IN_PROGRESS' or 'TASK_CREATED':
	# 		print(task_status)
	# 		time.sleep(10)
	# 	if task_status['status'] == 'TASK_DONE':
	# 		response = httpx.get(task_status["result_link"])
	# 		file_content = response.content
	# 		decoded_content = file_content.decode('utf-8')
	# 		return json.loads(decoded_content)