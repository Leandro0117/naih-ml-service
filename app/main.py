import os
from fastapi import FastAPI
from pydantic import BaseModel
from app.model_loader import load_or_download_model
from app.classifier import classify_text_sync

app = FastAPI()
MODEL_PATH = "/app/model"

# Cargar modelo al iniciar (puede descargarlo desde MODEL_URL)
MODEL_URL = os.environ.get("MODEL_URL")  # define en Railway
model, tokenizer = load_or_download_model(MODEL_PATH, MODEL_URL)

class Req(BaseModel):
    text: str

@app.post("/classify")
async def classify(payload: Req):
    text = payload.text
    category, confidence = classify_text_sync(model, tokenizer, text)
    return {"category": category, "confidence": confidence}
