from unittest.mock import patch

from fastapi.testclient import TestClient
from sqlalchemy.exc import OperationalError

from app.main import app

client = TestClient(app)


def test_live():
    response = client.get("/health/live")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    assert response.headers["X-Request-ID"]


def test_ready_unavailable():
    with patch("app.main.engine.connect", side_effect=OperationalError("", {}, Exception())):
        response = client.get("/health/ready")
    assert response.status_code == 503


def test_ready_database():
    response = client.get("/health/ready")
    assert response.status_code == 200
