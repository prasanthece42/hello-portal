from fastapi.testclient import TestClient

from app.main import app


def test_health_and_api():
    with TestClient(app) as client:
        assert client.get("/health").json() == {"status": "ok"}
        assert client.get("/api/message").json() == {
            "message": "Hello from Aegis!",
            "application": "hello-portal",
        }
        home = client.get("/")
        assert home.status_code == 200
        assert "Hello from my first app!" in home.text
