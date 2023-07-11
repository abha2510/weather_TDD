import json
import pytest
from app.weather import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_weather_by_city(client):
    response = client.get("/weather/San Francisco")
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert data == {'temperature': 14, 'weather': 'Cloudy'}

def test_add_weather_data(client):
    data = {
        "city": "Chicago",
        "temperature": 18,
        "weather": "Sunny"
    }
    response = client.post("/weather", json=data)
    assert response.status_code == 200
    assert json.loads(response.get_data(as_text=True)) == {"message": "Weather data added successfully"}

def test_update_weather_data(client):
    data = {
        "temperature": 25
    }
    response = client.put("/weather/San Francisco", json=data)
    assert response.status_code == 200
    assert json.loads(response.get_data(as_text=True)) == {"message": "Weather data updated successfully"}

def test_delete_weather_data(client):
    response = client.delete("/weather/San Francisco")
    assert response.status_code == 200
    assert json.loads(response.get_data(as_text=True)) == {"message": "Weather data deleted successfully"}


