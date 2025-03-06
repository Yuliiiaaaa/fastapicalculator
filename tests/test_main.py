from fastapi.testclient import TestClient 
from src.main import app

client = TestClient(app)

def test_add():
    response = client.post("/calculate", json={"operation_type": "add", "x": 5, "y": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_subtract():
    response = client.post("/calculate", json={"operation_type": "subtract", "x": 10, "y": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 6}

def test_multiply():
    response = client.post("/calculate", json={"operation_type": "multiply", "x": 2, "y": 6})
    assert response.status_code == 200
    assert response.json() == {"result": 12}

def test_divide():
    response = client.post("/calculate", json={"operation_type": "divide", "x": 15, "y": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_divide_by_zero():
    response = client.post("/calculate", json={"operation_type": "divide", "x": 10, "y": 0})
    assert response.status_code == 200
    assert response.json() == {"error": "Cannot divide by zero"}

def test_square_root():
    response = client.post("/calculate", json={"operation_type": "square_root", "x": 9})
    assert response.status_code == 200
    assert response.json() == {"result": 3.0}

def test_square_root_negative():
    response = client.post("/calculate", json={"operation_type": "square_root", "x": -1})
    assert response.status_code == 200
    assert response.json() == {"error": "Cannot take square root of a negative number"}

def test_invalid_operation():
    response = client.post("/calculate", json={"operation_type": "unknown", "x": 5, "y": 3})
    assert response.status_code == 200
    assert response.json() == {"error": "Invalid operation type"}