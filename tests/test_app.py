import pytest
from app import app


@pytest.fixture
def client():
    with app.test.client() as client:
        yield client


def test_get_weather_returns_200(client):
    response = client.get("/weather/San Francisco")
    assert response.status_code == 200


def test_create_weather_returns_201(client):
    data = {"city": "mumbai", "temperature": 18, 'weather': 'Cloudy'}
    response = client.post("/weather", json=data)
    assert response.status_code == 201


def test_update_weather_returns_200(client):
    data = {"temperature": 51, }
    response = client.put("/weather/mumbai", json=data)
    assert response.status_code == 200


def test_delete_weather_returns_204(client):
    response = client.delete("/weather/mumbai")
    assert response.status_code == 204
