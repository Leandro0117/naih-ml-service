import os
import requests
import tarfile
from pathlib import Path

def download_and_extract(url, dest):
    resp = requests.get(url, stream=True)
    tar_path = "/tmp/model.tar.gz"
    with open(tar_path, "wb") as f:
        for chunk in resp.iter_content(8192):
            f.write(chunk)
    Path(dest).mkdir(parents=True, exist_ok=True)
    with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(dest)

def load_or_download_model(dest_path, model_url=None):
    # Si el modelo ya está en disk, cargarlo; si no, descargarlo desde model_url
    if model_url and (not os.path.exists(dest_path) or not os.listdir(dest_path)):
        download_and_extract(model_url, dest_path)
    # aquí cargas con transformers
    from transformers import BertForSequenceClassification, BertTokenizer
    model = BertForSequenceClassification.from_pretrained(dest_path)
    tokenizer = BertTokenizer.from_pretrained(dest_path)
    return model, tokenizer
