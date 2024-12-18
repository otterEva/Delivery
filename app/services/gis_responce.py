import httpx
import json
import asyncio
from app.exceptions import GisException, JsonDecodeException, BaseAppException, CheckStatusException
from fastapi import HTTPException, status

class GetGisResponce:

	headers = {"Content-Type": "application/json"}
	api_key = "d7d625b0-6754-4633-8ad0-107de6cecc40"
	url_to_send_request = 'https://routing.api.2gis.com/async_matrix/create_task/get_dist_matrix?key='
	url_to_check_request_status = 'https://routing.api.2gis.com/async_matrix/result/get_dist_matrix/'
	
	async def get_2gis_responce(self, request):

		async with httpx.AsyncClient() as client:
			try:
				responce = await client.post(url = f"{self.url_to_send_request}{self.api_key}&version=2.0",
													headers = self.headers, json=request)
				task_id = responce.json()

			except httpx.HTTPError as e:
					raise GisException(message = 'Send task exception',
										exception = e,
										extradata = {"request" : request})
			except json.JSONDecodeError as e:
					raise JsonDecodeException(exception = e, extradata = responce)
			except Exception as e:
					raise BaseAppException(message = 'Unknown get_2gis_responce exception', exception = e)

			
			while True:
				try:
					responce = await client.get(url = f'{self.url_to_check_request_status}{task_id["task_id"]}?key={self.api_key}',
														headers = self.headers)
					task_status = responce.json()

					try:
						if task_status["status"] == 'TASK_CANCELED':
							return "задача отменена"
						elif task_status["status"] in ['TASK_IN_QUEUE', 'TASK_IN_PROGRESS', 'TASK_CREATED']:
							await asyncio.sleep(10)
						elif task_status['status'] == 'TASK_DONE':
							response = await client.get(task_status["result_link"])
							file_content = response.content
							decoded_content = file_content.decode('utf-8')
							return json.loads(decoded_content)
						else:
							raise HTTPException(status_code = status.HTTP_406_NOT_ACCEPTABLE, detail = 'неверный запрос')
						
					except Exception as e:
						raise CheckStatusException(exception = e, extradata = str(task_status))

				except httpx.HTTPError as e:
					raise GisException(message = 'Scheck task status exception',
										exception = e,
										extradata = {"request" : request, "task_id" : task_id})
				except json.JSONDecodeError as e:
						raise JsonDecodeException(exception = e, extradata = responce)
				except CheckStatusException as e:
					raise e
				except Exception as e:
						raise BaseAppException(message = 'Unknown exception', exception = str(e))

ResponceService = GetGisResponce()