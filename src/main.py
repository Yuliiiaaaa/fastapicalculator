from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Operation(BaseModel):
    operation_type: str
    x: float
    y: float = None


@app.post("/calculate")
async def calculate(operation: Operation):
    operation_type = operation.operation_type
    x = operation.x
    y = operation.y

    result = None

    if operation_type == "add":
        result = x + y
    elif operation_type == "subtract":
        result = x - y
    elif operation_type == "multiply":
        result = x * y
    elif operation_type == "divide":
        if y == 0:
            return {"error": "Cannot divide by zero"}
        result = x / y
    elif operation_type == "square_root":
        if x < 0:
            return {"error": "Cannot take square root of a negative number"}
        result = x ** 0.5
    else:
        return {"error": "Invalid operation type"}
    return {"result": result}
