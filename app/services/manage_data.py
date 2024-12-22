class UpdateDataService:

	def update_dataholder(self, dataholder, ready_responce):

		for responce in ready_responce["routes"]:

			real_sources = responce[1]["real_sources"]
			real_tagrets = responce[1]["real_targets"]

			j=0

			for route in responce[0]['routes']:
				distance_ =  route["distance"]
				duration_ =  route["duration"]
				dataholder[real_sources]['object'].distance[real_tagrets[j]] = distance_
				dataholder[real_sources]['object'].duration[real_tagrets[j]] = duration_
				j += 1

		return dataholder

DataManageService = UpdateDataService()