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