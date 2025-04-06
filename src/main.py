from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Union


app = FastAPI()  # Создание экземпляра приложения FastAPI


class CalculationRequest(BaseModel):  # Определение модели запроса
    operation: str
    a: float
    b: float


@app.post("/calculate/")
def calculate(
    request: CalculationRequest
) -> Union[Dict[str, float], Dict[str, str]]:
    if request.operation == "add":
        return {"result": request.a + request.b}
    elif request.operation == "subtract":
        return {"result": request.a - request.b}
    elif request.operation == "multiply":
        return {"result": request.a * request.b}
    elif request.operation == "divide":
        if request.b == 0:
            return {"error": "Division by zero is not allowed."}
        return {"result": request.a / request.b}
    else:
        return {"error": "Unsupported operation."}


if __name__ == "__main__":  # Запуск приложения
    import uvicorn
    uvicorn.run(app, host="194.226.28.81", port=8000)
