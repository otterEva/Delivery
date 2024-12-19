import app.schemas.request_schemas as schema

class PrepareApiRequestService:
    
    def prepare_request(self, delivery_request: schema.DeliveryRequestSchema):
        return self._create_data_structure(delivery_request)

    def _create_data_structure(self, delivery_request: schema.DeliveryRequestSchema):

            data = {}
            index = 1

            for courier in delivery_request.couriers:
                data[index] = {"object_type": 1, "object": courier}
                index += 1


            for order in delivery_request.orders:
                data[index] = {"object_type": 2, "object": order}
                relative_index = index
                index += 1

                for suborder in order.suborders:
                    data[index] = {
                        "object_type": 3,
                        "object": suborder,
                        "relative": relative_index
                    }
                    index += 1

            return self._get_permutations(data)
            
    def _get_permutations(self, data):
        

        from_list = []
        to_list = []

        for first_object in data:
            for second_object in data:
                if second_object == first_object:
                    continue
                if data[first_object]["object_type"] == 1 and data[second_object]["object_type"] == 1:
                    continue
                if data[first_object]["object_type"] == 2 and data[second_object]["object_type"] == 1:
                    continue
                if data[first_object]["object_type"] == 3 and data[second_object]["object_type"] == 1:
                    continue
                if data[first_object]["object_type"] == 2 and data[second_object]["object_type"] == 3 and (
                                    data[second_object]["relative"] == first_object):
                    continue
                
                from_list.append((first_object, data[first_object]["object"]))
                to_list.append((second_object, data[second_object]["object"]))

        from_sublist = [from_list[i:i + 10] for i in range(0, len(from_list), 10)]
        to_sublist = [to_list[i:i + 10] for i in range(0, len(to_list), 10)]

        request_list = []
        for from_list, to_list in zip(from_sublist, to_sublist):
            request_list.append(self._prepare_request(from_list,  to_list))

        return request_list

    def _prepare_request(self, from_list, to_list):

        points = []
        
        pairs = list(zip(from_list, to_list))

        for from_, to_ in pairs:
            if isinstance(from_[1], schema.Courier) or isinstance(from_[1], schema.SubOrder):
                points.append({"lat": from_[1].address[0], "lon": from_[1].address[1]})
            if isinstance(from_[1], schema.Order):
                points.append({"lat": from_[1].order.address[0], "lon": from_[1].order.address[1]})

            if isinstance(to_[1], schema.Courier) or isinstance(to_[1], schema.SubOrder):
                points.append({"lat": to_[1].address[0], "lon": to_[1].address[1]})
            if isinstance(to_, schema.Order):
                points.append({"lat": to_[1].order.address[0], "lon": to_[1].order.address[1]})

        ready_api_request = {
            "points": points,
            "sources": [element[0] for element in from_list],
            "targets": [element[0] for element in to_list],
            "type": "jam"
        }

        return ready_api_request

RequestService = PrepareApiRequestService()