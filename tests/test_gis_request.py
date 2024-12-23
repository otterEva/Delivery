import pytest
from app.services.gis_request import PrepareApiRequestService
from app.schemas.request_schemas import Courier, OrderData, SubOrder


class TestPrepareApiRequestService:

    def test__get_permutations(self):
        data = {
            0: {
                "object_type": 1,
                "object": Courier(
                    courier_id=1,
                    address=(55.75, 37.62),
                    duration={},
                    distance={},
                ),
            },
            1: {
                "object_type": 2,
                "object": OrderData(
                    address=(55.76, 37.63),
                    duration={},
                    distance={},
                ),
            },
            2: {
                "object_type": 2,
                "object": OrderData(
                    address=(55.77, 37.64),
                    duration={},
                    distance={},
                ),
            },
            3: {
                "object_type": 3,
                "relative": 2,
                "object": SubOrder(
                    address=(55.78, 37.65),
                    items={},
                    duration={},
                    distance={},
                )
            },
        }

        service = PrepareApiRequestService()
        request_list = service._get_permutations(data)

        assert request_list, "Список permutations пуст, хотя должен содержать хотя бы один запрос."

        for req in request_list:
            assert "points" in req
            assert "sources" in req
            assert "targets" in req
            assert "real_sources" in req
            assert "real_targets" in req

            assert isinstance(req["points"], list)
            for p in req["points"]:
                assert "lat" in p
                assert "lon" in p
