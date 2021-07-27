from fastapi.testclient import TestClient
from src.pymsys import ExampleNode, Server


app = Server(ExampleNode)

client = TestClient(app)


def test_get_config():
    response = client.get("/config")
    assert response.status_code == 200
    assert response.json() != {}


def test_configure():
    response = client.post("/config",
                           json={},)
    assert response.status_code == 200
    assert response.json() != {}


def test_update():
    response = client.put("/update",
                          json={},)
    assert response.status_code == 200
    assert response.json() != {}

