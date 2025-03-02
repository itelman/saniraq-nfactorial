# Используем официальный образ Python 3.12 slim
FROM python:3.12-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Применяем миграции Alembic
RUN alembic upgrade head

# Открываем порт, на котором будет работать FastAPI
EXPOSE 8000

# Запускаем Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]