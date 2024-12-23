import app.schemas.request_schemas as schema

class PrepareApiRequestService:
    
    def prepare_request(self, delivery_request: schema.DeliveryRequestSchema):
        return self._create_data_structure(delivery_request)

    def _create_data_structure(self, delivery_request: schema.DeliveryRequestSchema):

            data = {}
            index = 0

            for courier in delivery_request.couriers:
                data[index] = {"object_type": 1, "object": courier}
                index += 1

            for order in delivery_request.orders:
                data[index] = {"object_type": 2, "object": order.order}
                relative_index = index
                index += 1

                for suborder in order.suborders:
                    data[index] = {
                        "object_type": 3,
                        "object": suborder,
                        "relative": relative_index
                    }
                    index += 1

            return self._get_permutations(data), data
            
    def _get_permutations(self, data):
        

        from_list = []
        to_list = []

        for first_object in data:
            for second_object in data:
                if second_object == first_object:
                    continue
                if data[first_object]["object_type"] == 1 and data[second_object]["object_type"] == 1:
                    continue
                if data[first_object]["object_type"] == 1 and data[second_object]["object_type"] == 2:
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

    
        from_sublist, to_sublist = self._get_to_and_from_sublists(to_list, from_list)

        request_list = []

        for from_list, to_list in zip(from_sublist, to_sublist):
            request_list.append(self._prepare_request(from_list,  to_list))

        return request_list

    def _prepare_request(self, from_list, to_list):

        points = []
        first = from_list[0][0]
        second = []
        sources = []
        targets = []

        points.append({"lat": from_list[0][1].address[0], "lon": from_list[0][1].address[1]})
        sources.append(0)

        i=1

        for to_ in to_list:
            
            points.append({"lat": to_[1].address[0], "lon": to_[1].address[1]})
            second.append(to_[0])
            targets.append(i)
            i += 1

        ready_api_request = {
            "points": points,

            "sources": sources,
            "targets": targets,

            "real_sources" : first,
            "real_targets" : second
        }

        return ready_api_request
    
    ########################################################################################################
    
    def _get_to_and_from_sublists(self, to_list, from_list):
        from_sublist = self._get_from_sublist(from_list)
        to_sublist = []
        index = 0
        for sublist in from_sublist:
            count = len(sublist)
            to_sublist.append(to_list[index:index + count])
            index += count

        return from_sublist, to_sublist
    
    def _get_from_sublist(self, from_list):

        from_sublist = []
        sublist = []
        e = 0

        for i in range(1, len(from_list)):
            if from_list[i] == from_list[i - 1] and e < 9:
                e += 1
                sublist.append(from_list[i - 1])
            else:
                sublist.append(from_list[i - 1])
                from_sublist.append(sublist)
                sublist = []
                e = 0

        if sublist:
            sublist.append(from_list[-1])
            from_sublist.append(sublist)

        return from_sublist


RequestService = PrepareApiRequestService()