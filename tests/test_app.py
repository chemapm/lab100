from app.models import Data
from app import create_app, db
from tests import SqLiteTestConfig
import pytest


@pytest.fixture
def app():
    app = create_app(SqLiteTestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


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


def test_data_model():
    data = Data(name="Test Data")
    assert data.name == "Test Data"
