from app.schemas.request_schemas import DeliveryRequestSchema
from itertools import permutations

def get_distances_and_durations(data: DeliveryRequestSchema):
    points = []
    for courier in data.couriers:
        points.append([courier.courier_address, courier])
    for client in data.orders:
        points.append([client.delivery_address, client])
        for suborder in client.suborders:
            points.append([suborder.warehouse_address, suborder])
    return points

def get_permutations(points):
    return list(permutations(points, 2))
def transform_data(data):

    points = []
    sources = []
    targets = []
    
    for i, pair in enumerate(data):
        for j, coord in enumerate(pair):
          points.append({"lat": coord[0], "lon": coord[1]})
          if j == 0:
             sources.append(len(points) - 1)
          elif j == 1:
             targets.append(len(points) - 1)

    result = {
        "points": points,
        "sources": sources,
        "targets": targets,
        "type": "jam"
    }
    return result