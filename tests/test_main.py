from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)  # Создается экземпляр TestClient


def test_add():
    response = client.post(
        "/calculate/",
        json={"operation": "add", "a": 1, "b": 2}
    )
    assert response.status_code == 200
    assert response.json() == {"result": 3}


def test_subtract():
    response = client.post(
        "/calculate/",
        json={"operation": "subtract", "a": 5, "b": 2}
    )
    assert response.status_code == 200
    assert response.json() == {"result": 3}


def test_multiply():
    response = client.post(
        "/calculate/",
        json={"operation": "multiply", "a": 3, "b": 4}
    )
    assert response.status_code == 200
    assert response.json() == {"result": 12}


def test_divide():
    response = client.post(
        "/calculate/",
        json={"operation": "divide", "a": 10, "b": 2}
    )
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_divide_by_zero():
    response = client.post(
        "/calculate/",
        json={"operation": "divide", "a": 10, "b": 0}
    )
    assert response.status_code == 200
    assert response.json() == {
        "error": "Division by zero is not allowed."
    }


def test_unsupported_operation():
    response = client.post(
        "/calculate/",
        json={"operation": "modulus", "a": 10, "b": 3}
    )
    assert response.status_code == 200
    assert response.json() == {"error": "Unsupported operation."}
