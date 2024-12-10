# Библиотека для имитации HTTP-запросов к приложению FastAPI
from fastapi.testclient import TestClient

#Импортируем приложение FastAPI из main
from app.main import app

#Выполнение тестового HTTP-запроса в локальной памяти (без запуска реального сервера)

#Создаем клиента для взаимодействия с приложением
client = TestClient(app)

def test_calculate_route():
    request_data = {
        "courier_start_point": [55.7558, 37.6173],
        "delivery_points": [
            {
                "coordinates": [55.7522, 37.6156],
                "items": [
                    {"guid": "item1", "quantity": 2}
                ]
            }
        ],
        "warehouses": [
            {
                "coordinates": [55.7602, 37.6225],
                "items": ["item1"]
            }
        ],
        "courier_capacity": 10
    }

    response = client.post("/api/calculate_route", json=request_data) #Отправляем HTTP POST-запрос на эндпоинт
    assert response.status_code == 200 #Проверка статуса ответа
    expected_response = {
        "route": [
            [55.7602, 37.6225],
            [55.7522, 37.6156],
            [55.7558, 37.6173]
        ],
        "map_url": "http://example.com/map"
    }
    assert response.json() == expected_response
