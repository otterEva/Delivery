from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


dataholder = {
    "0": {
        "object_type": 1,
        "object": {
            "courier_id": 1,
            "address": [55.8767058758, 37.3120502],
            "duration": {
                "4": 549,
                "5": 2425,
                "7": 1849,
                "8": 2265,
                "9": 2235,
                "11": 318,
            },
            "distance": {
                "4": 2651,
                "5": 21531,
                "7": 20223,
                "8": 24146,
                "9": 24675,
                "11": 1549,
            },
        },
    },
    "1": {
        "object_type": 1,
        "object": {
            "courier_id": 2,
            "address": [54.845705875, 37.325302],
            "duration": {
                "4": 7410,
                "5": 7651,
                "7": 7044,
                "8": 7563,
                "9": 7650,
                "11": 7317,
            },
            "distance": {
                "4": 141756,
                "5": 145818,
                "7": 144449,
                "8": 148372,
                "9": 148901,
                "11": 142034,
            },
        },
    },
    "2": {
        "object_type": 1,
        "object": {
            "courier_id": 3,
            "address": [54.8578058, 37.338028],
            "duration": {
                "4": 7341,
                "5": 7562,
                "7": 7010,
                "8": 7488,
                "9": 7580,
                "11": 7248,
            },
            "distance": {
                "4": 139842,
                "5": 143904,
                "7": 142535,
                "8": 146458,
                "9": 146987,
                "11": 140120,
            },
        },
    },
    "3": {
        "object_type": 2,
        "object": {
            "address": [55.8625058, 37.31502868],
            "duration": {
                "6": 644,
                "7": 1801,
                "8": 2231,
                "9": 2194,
                "10": 1836,
                "11": 310,
            },
            "distance": {
                "6": 5514,
                "7": 19791,
                "8": 23714,
                "9": 24243,
                "10": 24225,
                "11": 2100,
            },
        },
    },
    "4": {
        "object_type": 3,
        "object": {
            "address": [55.879705, 37.331028],
            "items": {"5": 1, "16": 1, "28": 2, "68": 7},
            "duration": {
                "3": 454,
                "5": 2246,
                "6": 427,
                "7": 1646,
                "8": 2080,
                "9": 2053,
                "10": 1690,
                "11": 344,
            },
            "distance": {
                "3": 3269,
                "5": 20631,
                "6": 3112,
                "7": 19323,
                "8": 23246,
                "9": 23775,
                "10": 23757,
                "11": 2015,
            },
        },
        "relative": 3,
    },
    "5": {
        "object_type": 3,
        "object": {
            "address": [55.8843705, 37.355028],
            "items": {"127": 10},
            "duration": {
                "3": 1815,
                "4": 1887,
                "6": 1968,
                "7": 777,
                "8": 1054,
                "9": 1415,
                "10": 1685,
                "11": 1805,
            },
            "distance": {
                "3": 15888,
                "4": 15795,
                "6": 18162,
                "7": 4399,
                "8": 7058,
                "9": 11623,
                "10": 17152,
                "11": 16128,
            },
        },
        "relative": 3,
    },
    "6": {
        "object_type": 2,
        "object": {
            "address": [55.8917058, 37.3150286],
            "duration": {"3": 788, "4": 755, "5": 2668, "10": 2092, "11": 660},
            "distance": {"3": 7109, "4": 5591, "5": 24471, "10": 27597, "11": 5855},
        },
    },
    "7": {
        "object_type": 3,
        "object": {
            "address": [55.91077058, 37.3650286],
            "items": {"16": 5, "23": 1},
            "duration": {
                "3": 1354,
                "4": 1393,
                "5": 794,
                "6": 1514,
                "8": 527,
                "9": 714,
                "10": 978,
                "11": 1336,
            },
            "distance": {
                "3": 16571,
                "4": 16478,
                "5": 4399,
                "6": 18845,
                "8": 4919,
                "9": 8220,
                "10": 12165,
                "11": 16811,
            },
        },
        "relative": 6,
    },
    "8": {
        "object_type": 3,
        "object": {
            "address": [55.9227, 37.331028686],
            "items": {"12": 4},
            "duration": {
                "3": 1848,
                "4": 1883,
                "5": 1104,
                "6": 2041,
                "7": 569,
                "9": 1179,
                "10": 1466,
                "11": 1817,
            },
            "distance": {
                "3": 20547,
                "4": 20454,
                "5": 7111,
                "6": 22821,
                "7": 4972,
                "9": 12196,
                "10": 16141,
                "11": 20787,
            },
        },
        "relative": 6,
    },
    "9": {
        "object_type": 3,
        "object": {
            "address": [55.9337058, 37.3450286],
            "items": {"67": 1, "374": 2, "1235": 2, "4536": 10, "12352": 1},
            "duration": {
                "3": 1743,
                "4": 1807,
                "5": 1385,
                "6": 1924,
                "7": 707,
                "8": 1124,
                "10": 1065,
                "11": 1743,
            },
            "distance": {
                "3": 20994,
                "4": 20901,
                "5": 11511,
                "6": 23268,
                "7": 8108,
                "8": 12031,
                "10": 10592,
                "11": 21234,
            },
        },
        "relative": 6,
    },
    "10": {
        "object_type": 2,
        "object": {
            "address": [55.9410705, 37.35992868],
            "duration": {
                "3": 1370,
                "4": 1390,
                "5": 1510,
                "6": 1526,
                "7": 905,
                "8": 1319,
                "9": 1194,
            },
            "distance": {
                "3": 20489,
                "4": 20396,
                "5": 16176,
                "6": 22763,
                "7": 14660,
                "8": 18583,
                "9": 17796,
            },
        },
    },
    "11": {
        "object_type": 3,
        "object": {
            "address": [55.867058, 37.32502868],
            "items": {"5": 3},
            "duration": {
                "3": 304,
                "4": 432,
                "5": 2266,
                "6": 518,
                "7": 1672,
                "8": 2092,
                "9": 2085,
                "10": 1715,
            },
            "distance": {
                "3": 2100,
                "4": 1948,
                "5": 20828,
                "6": 4260,
                "7": 19520,
                "8": 23443,
                "9": 23972,
                "10": 23954,
            },
        },
        "relative": 10,
    },
}


def create_data_objects(dataholder):
    vector = len(dataholder)
    matrix = []
    couriers = []
    dependencies = {}

    for _ in range(vector):
        matrix.append([0 * vector] * vector)

    for key, value in dataholder.items():
        key = int(key)

        for i in range(vector):
            if key == i:
                matrix[key][i] = None
            else:
                fool = value["object"]["distance"]
                if str(i) in fool and fool[str(i)] != 0:
                    matrix[key][int(i)] = value["object"]["distance"][str(i)]
                else:
                    matrix[key][int(i)] = None
        type_ = value["object_type"]

        if type_ == 1:
            couriers.append(key)
        if type_ == 3:
            dependencies[key] = value["relative"]

    return matrix, couriers, dependencies


matrix, couriers, dependencies = create_data_objects(dataholder)
