FROM pytorch/pytorch:2.2.1-cuda11.8-cudnn8-runtime  # si quieres GPU; si no, usa python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# puerto que Railway asignará vía $PORT; uvicorn puede usar 8000 por defecto
CMD ["bash", "-lc", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1"]
