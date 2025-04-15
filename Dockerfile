# Базовый образ Python с легковесной ОС
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только файлы зависимостей сначала (для оптимизации кэша)
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Устанавливаем переменные окружения
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Команда для запуска приложения
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]