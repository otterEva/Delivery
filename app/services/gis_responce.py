import httpx
import json
import asyncio
from app.config import settings

class GetGisResponce:
	
	headers = {"Content-Type": "application/json"}
	api_key = settings.app.api_key
	url_to_send_request = 'https://routing.api.2gis.com/async_matrix/create_task/get_dist_matrix?key='
	url_to_check_request_status = 'https://routing.api.2gis.com/async_matrix/result/get_dist_matrix/'

	async def gather_2gis_list_responce(self, request_list):
		async with httpx.AsyncClient() as client:
			responce_list = await asyncio.gather(*[self._get_2gis_responce(client, request) for request in request_list])

		combined_routes = []

		for entry in responce_list:
			combined_routes.extend(entry["routes"])

		return {"routes": combined_routes}
	
	async def _get_2gis_responce(self, client, request):
		responce = await client.post(url=f"{self.url_to_send_request}{self.api_key}&version=2.0",
									  headers=self.headers, json=request)
		task_id = responce.json()
		print(task_id)

		while True:
			responce = await client.get(url=f'{self.url_to_check_request_status}{task_id["task_id"]}?key={self.api_key}',
										 headers=self.headers)
			task_status = responce.json()
			print(task_status)

			if task_status["status"] == 'TASK_CANCELED':
				return "задача отменена"
			elif task_status["status"] in ['TASK_IN_QUEUE', 'TASK_IN_PROGRESS', 'TASK_CREATED']:
				await asyncio.sleep(10)
			elif task_status['status'] == 'TASK_DONE':
				response = await client.get(task_status["result_link"])
				file_content = response.content
				decoded_content = file_content.decode('utf-8')
				return json.loads(decoded_content)

ResponceService = GetGisResponce()