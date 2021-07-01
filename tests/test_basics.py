from fastapi.testclient import TestClient
from src.pymsys import ExampleModule, Server


app = Server(ExampleModule)

client = TestClient(app)


def test_get_config():
    response = client.get("/config")
    assert response.status_code == 200
    assert response.json() != {}


def test_configure():
    response = client.post("/config",
                           json={"id": "test"},)
    assert response.status_code == 200
    assert response.json() != {}


def test_update():
    response = client.put("/update",
                          json={"id": "foobar"},)
    assert response.status_code == 200
    assert response.json() != {}

