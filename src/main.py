from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict


app = FastAPI()


class Operation(BaseModel):
    operation_type: str
    x: float
    y: float = None


@app.post("/calculate")
async def calculate(operation: Operation) -> Dict[str, str]:
    operation_type = operation.operation_type
    x = operation.x
    y = operation.y

    try:
        if operation_type == "add":
            result = x + y
        elif operation_type == "subtract":
            result = x - y
        elif operation_type == "multiply":
            result = x * y
        elif operation_type == "divide":
            if y == 0:
                raise ValueError("Cannot divide by zero")
            result = x / y
        elif operation_type == "square_root":
            if x < 0:
                raise ValueError("square root of a negative number")
            result = x * 0.5
        else:
            raise ValueError("Invalid operation type")
        return {"result": str(result)}
    except ValueError as e:
        return {"error": str(e)}
