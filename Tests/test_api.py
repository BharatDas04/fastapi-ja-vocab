import sys
sys.path.append("./")
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_health_check():
    res = client.get("/healthz")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_get_demo_token():
    res = client.post("/demo_token")
    assert res.status_code == 200
    data = res.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
