import pytest
from app.services.algorithm import create_data_objects


@pytest.fixture
def sample_dataholder():
    return {
        "0": {
            "object_type": 1,
            "object": {
                "distance": {"1": 100, "2": 200},
                "duration": {"1": 10, "2": 20}
            }
        },
        "1": {
            "object_type": 2,
            "object": {
                "distance": {"0": 100, "2": 300},
                "duration": {"0": 15, "2": 35}
            }
        },
        "2": {
            "object_type": 3,
            "relative": 1,
            "object": {
                "distance": {"0": 200},
                "duration": {"0": 25}
            }
        }
    }


def test_create_data_objects(sample_dataholder):
    matrix, couriers, dependencies = create_data_objects(sample_dataholder)
    assert len(matrix) == 3
    assert all(len(row) == 3 for row in matrix), "Каждая строка должна быть длины 3"
    assert couriers == [0]
    assert dependencies[2] == 1

    assert matrix[0][0] is None
    assert matrix[0][1] == 100
    assert matrix[0][2] == 200

    assert matrix[1][1] is None
    assert matrix[1][0] == 100
    assert matrix[1][2] == 300

    assert matrix[2][2] is None
    assert matrix[2][0] == 200
    assert matrix[2][1] is None
