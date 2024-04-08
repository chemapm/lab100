# tests/test_app.py
from app.models import Data
from app import create_app, db
import json


def test_insert_data(client):
    data = {"name": "Test Data"}
    response = client.post('/data', json=data)
    assert response.status_code == 200
    assert response.json == {"message": "Data inserted successfully"}


def test_get_all_data(client):
    response = client.get('/data')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_delete_data(client):
    data = {"name": "Test Data"}
    client.post('/data', json=data)  # Inserting test data
    data_id = Data.query.filter_by(name=data['name']).first().id
    response = client.delete(f'/data/{data_id}')
    assert response.status_code == 200
    assert response.json == {"message": "Data deleted successfully"}


# tests/test_models.py
from app.models import Data


def test_data_model():
    data = Data(name="Test Data")
    assert data.name == "Test Data"
