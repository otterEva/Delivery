from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

dataholder = {
  "0": {
    "object_type": 1,
    "object": {
      "courier_id": 1,
      "address": [
        55.8767058758,
        37.3120502
      ],
      "duration": {
        "4": 549,
        "5": 2425,
        "7": 1849,
        "8": 2265,
        "9": 2235,
        "11": 318
      },
      "distance": {
        "4": 2651,
        "5": 21531,
        "7": 20223,
        "8": 24146,
        "9": 24675,
        "11": 1549
      }
    }
  },
  "1": {
    "object_type": 1,
    "object": {
      "courier_id": 2,
      "address": [
        54.845705875,
        37.325302
      ],
      "duration": {
        "4": 7410,
        "5": 7651,
        "7": 7044,
        "8": 7563,
        "9": 7650,
        "11": 7317
      },
      "distance": {
        "4": 141756,
        "5": 145818,
        "7": 144449,
        "8": 148372,
        "9": 148901,
        "11": 142034
      }
    }
  },
  "2": {
    "object_type": 1,
    "object": {
      "courier_id": 3,
      "address": [
        54.8578058,
        37.338028
      ],
      "duration": {
        "4": 7341,
        "5": 7562,
        "7": 7010,
        "8": 7488,
        "9": 7580,
        "11": 7248
      },
      "distance": {
        "4": 139842,
        "5": 143904,
        "7": 142535,
        "8": 146458,
        "9": 146987,
        "11": 140120
      }
    }
  },
  "3": {
    "object_type": 2,
    "object": {
      "address": [
        55.8625058,
        37.31502868
      ],
      "duration": {
        "6": 644,
        "7": 1801,
        "8": 2231,
        "9": 2194,
        "10": 1836,
        "11": 310
      },
      "distance": {
        "6": 5514,
        "7": 19791,
        "8": 23714,
        "9": 24243,
        "10": 24225,
        "11": 2100
      }
    }
  },
  "4": {
    "object_type": 3,
    "object": {
      "address": [
        55.879705,
        37.331028
      ],
      "items": {
        "5": 1,
        "16": 1,
        "28": 2,
        "68": 7
      },
      "duration": {
        "3": 454,
        "5": 2246,
        "6": 427,
        "7": 1646,
        "8": 2080,
        "9": 2053,
        "10": 1690,
        "11": 344
      },
      "distance": {
        "3": 3269,
        "5": 20631,
        "6": 3112,
        "7": 19323,
        "8": 23246,
        "9": 23775,
        "10": 23757,
        "11": 2015
      }
    },
    "relative": 3
  },
  "5": {
    "object_type": 3,
    "object": {
      "address": [
        55.8843705,
        37.355028
      ],
      "items": {
        "127": 10
      },
      "duration": {
        "3": 1815,
        "4": 1887,
        "6": 1968,
        "7": 777,
        "8": 1054,
        "9": 1415,
        "10": 1685,
        "11": 1805
      },
      "distance": {
        "3": 15888,
        "4": 15795,
        "6": 18162,
        "7": 4399,
        "8": 7058,
        "9": 11623,
        "10": 17152,
        "11": 16128
      }
    },
    "relative": 3
  },
  "6": {
    "object_type": 2,
    "object": {
      "address": [
        55.8917058,
        37.3150286
      ],
      "duration": {
        "3": 788,
        "4": 755,
        "5": 2668,
        "10": 2092,
        "11": 660
      },
      "distance": {
        "3": 7109,
        "4": 5591,
        "5": 24471,
        "10": 27597,
        "11": 5855
      }
    }
  },
  "7": {
    "object_type": 3,
    "object": {
      "address": [
        55.91077058,
        37.3650286
      ],
      "items": {
        "16": 5,
        "23": 1
      },
      "duration": {
        "3": 1354,
        "4": 1393,
        "5": 794,
        "6": 1514,
        "8": 527,
        "9": 714,
        "10": 978,
        "11": 1336
      },
      "distance": {
        "3": 16571,
        "4": 16478,
        "5": 4399,
        "6": 18845,
        "8": 4919,
        "9": 8220,
        "10": 12165,
        "11": 16811
      }
    },
    "relative": 6
  },
  "8": {
    "object_type": 3,
    "object": {
      "address": [
        55.9227,
        37.331028686
      ],
      "items": {
        "12": 4
      },
      "duration": {
        "3": 1848,
        "4": 1883,
        "5": 1104,
        "6": 2041,
        "7": 569,
        "9": 1179,
        "10": 1466,
        "11": 1817
      },
      "distance": {
        "3": 20547,
        "4": 20454,
        "5": 7111,
        "6": 22821,
        "7": 4972,
        "9": 12196,
        "10": 16141,
        "11": 20787
      }
    },
    "relative": 6
  },
  "9": {
    "object_type": 3,
    "object": {
      "address": [
        55.9337058,
        37.3450286
      ],
      "items": {
        "67": 1,
        "374": 2,
        "1235": 2,
        "4536": 10,
        "12352": 1
      },
      "duration": {
        "3": 1743,
        "4": 1807,
        "5": 1385,
        "6": 1924,
        "7": 707,
        "8": 1124,
        "10": 1065,
        "11": 1743
      },
      "distance": {
        "3": 20994,
        "4": 20901,
        "5": 11511,
        "6": 23268,
        "7": 8108,
        "8": 12031,
        "10": 10592,
        "11": 21234
      }
    },
    "relative": 6
  },
  "10": {
    "object_type": 2,
    "object": {
      "address": [
        55.9410705,
        37.35992868
      ],
      "duration": {
        "3": 1370,
        "4": 1390,
        "5": 1510,
        "6": 1526,
        "7": 905,
        "8": 1319,
        "9": 1194
      },
      "distance": {
        "3": 20489,
        "4": 20396,
        "5": 16176,
        "6": 22763,
        "7": 14660,
        "8": 18583,
        "9": 17796
      }
    }
  },
  "11": {
    "object_type": 3,
    "object": {
      "address": [
        55.867058,
        37.32502868
      ],
      "items": {
        "5": 3
      },
      "duration": {
        "3": 304,
        "4": 432,
        "5": 2266,
        "6": 518,
        "7": 1672,
        "8": 2092,
        "9": 2085,
        "10": 1715
      },
      "distance": {
        "3": 2100,
        "4": 1948,
        "5": 20828,
        "6": 4260,
        "7": 19520,
        "8": 23443,
        "9": 23972,
        "10": 23954
      }
    },
    "relative": 10
  }
}

##################################################################################

def create_matrix(dataholder):

	vector = len(dataholder)
	matrix = []

	for _ in range(vector):
		matrix.append([0*vector]*vector)

	for key, value in dataholder.items():

		key = int(key)

		for i in range(vector):
			if key == i:
				matrix[key][i] = 0
			else:
				fool = value["object"]["distance"]
				if str(i) in fool and fool[str(i)] != 0:
					matrix[key][int(i)] = value["object"]["distance"][str(i)]
				else:
					matrix[key][int(i)] = 999999
                              
	for list_ in matrix:
		print(list_)
            
create_matrix(dataholder)

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data["distance_matrix"] = [
        # fmt: off
      [0, 548, 776, 696, 582, 274, 502, 194, 308, 194, 536, 502, 388, 354, 468, 776, 662],
      [548, 0, 684, 308, 194, 502, 730, 354, 696, 742, 1084, 594, 480, 674, 1016, 868, 1210],
      [776, 684, 0, 992, 878, 502, 274, 810, 468, 742, 400, 1278, 1164, 1130, 788, 1552, 754],
      [696, 308, 992, 0, 114, 650, 878, 502, 844, 890, 1232, 514, 628, 822, 1164, 560, 1358],
      [582, 194, 878, 114, 0, 536, 764, 388, 730, 776, 1118, 400, 514, 708, 1050, 674, 1244],
      [274, 502, 502, 650, 536, 0, 228, 308, 194, 240, 582, 776, 662, 628, 514, 1050, 708],
      [502, 730, 274, 878, 764, 228, 0, 536, 194, 468, 354, 1004, 890, 856, 514, 1278, 480],
      [194, 354, 810, 502, 388, 308, 536, 0, 342, 388, 730, 468, 354, 320, 662, 742, 856],
      [308, 696, 468, 844, 730, 194, 194, 342, 0, 274, 388, 810, 696, 662, 320, 1084, 514],
      [194, 742, 742, 890, 776, 240, 468, 388, 274, 0, 342, 536, 422, 388, 274, 810, 468],
      [536, 1084, 400, 1232, 1118, 582, 354, 730, 388, 342, 0, 878, 764, 730, 388, 1152, 354],
      [502, 594, 1278, 514, 400, 776, 1004, 468, 810, 536, 878, 0, 114, 308, 650, 274, 844],
      [388, 480, 1164, 628, 514, 662, 890, 354, 696, 422, 764, 114, 0, 194, 536, 388, 730],
      [354, 674, 1130, 822, 708, 628, 856, 320, 662, 388, 730, 308, 194, 0, 342, 422, 536],
      [468, 1016, 788, 1164, 1050, 514, 514, 662, 320, 274, 388, 650, 536, 342, 0, 764, 194],
      [776, 868, 1552, 560, 674, 1050, 1278, 742, 1084, 810, 1152, 274, 388, 422, 764, 0, 798],
      [662, 1210, 754, 1358, 1244, 708, 480, 856, 514, 468, 354, 844, 730, 536, 194, 798, 0],
        # fmt: on
    ]
    data["pickups_deliveries"] = [
        [1, 6],
        [2, 10],
        [4, 3],
        [5, 9],
        [7, 8],
        [15, 11],
        [13, 12],
        [16, 14],
    ]
    data["num_vehicles"] = 4
    data["depot"] = 0
    return data


def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    print(f"Objective: {solution.ObjectiveValue()}")
    total_distance = 0
    for vehicle_id in range(data["num_vehicles"]):
        index = routing.Start(vehicle_id)
        plan_output = f"Route for vehicle {vehicle_id}:\n"
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f" {manager.IndexToNode(index)} -> "
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id
            )
        plan_output += f"{manager.IndexToNode(index)}\n"
        plan_output += f"Distance of the route: {route_distance}m\n"
        print(plan_output)
        total_distance += route_distance
    print(f"Total Distance of all routes: {total_distance}m")


def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(
        len(data["distance_matrix"]), data["num_vehicles"], data["depot"]
    )

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Define cost of each arc.
    def distance_callback(from_index, to_index):
        """Returns the manhattan distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data["distance_matrix"][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    dimension_name = "Distance"
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        3000,  # vehicle maximum travel distance
        True,  # start cumul to zero
        dimension_name,
    )
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    # Define Transportation Requests.
    for request in data["pickups_deliveries"]:
        pickup_index = manager.NodeToIndex(request[0])
        delivery_index = manager.NodeToIndex(request[1])
        routing.AddPickupAndDelivery(pickup_index, delivery_index)
        routing.solver().Add(
            routing.VehicleVar(pickup_index) == routing.VehicleVar(delivery_index)
        )
        routing.solver().Add(
            distance_dimension.CumulVar(pickup_index)
            <= distance_dimension.CumulVar(delivery_index)
        )

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION
    )

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(data, manager, routing, solution)
