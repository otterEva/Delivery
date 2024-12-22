class UpdateDataService:

	def update_dataholder(self, dataholder, ready_responce):

		for responce in ready_responce["routes"]:
			source_id =  responce["source_id"]
			target_id =  responce["target_id"]
			distance_ =  responce["distance"]	
			duration_ =  responce["duration"]

			dataholder[source_id]["object"].distance[target_id] = distance_
			dataholder[source_id]["object"].duration[target_id] = duration_

		return dataholder


DataManageService = UpdateDataService()