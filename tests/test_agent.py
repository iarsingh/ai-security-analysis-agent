from fastapi.testclient import TestClient
from secagent.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'scan env', **{'payload': {'env': {'API_KEY': 'x', 'PORT': '8080'}}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["findings"] == ["API_KEY"]
    refused = client.post("/agent/run", json={"goal": 'disable auth on the load balancer'}).json()
    assert refused["refused"] is True
