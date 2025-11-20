#!/bin/bash
# descarga pre-start si quieres
python -c "from app.model_loader import load_or_download_model; load_or_download_model('/app/model', '${MODEL_URL:-}')" &
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
