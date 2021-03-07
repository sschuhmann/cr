from fastapi.testclient import TestClient
from mobility.main import app
import mobility.models as models
from . import helper

client = TestClient(app)
def setup_module(module):
    helper.clear_database_records()

def test_create_user():
    response = client.post('/users/',
                        json={"name": "Max Mustermann", "gender": "m", "age": 30, "mail": "mmustermann@mail.com"})

    assert response.status_code == 200
