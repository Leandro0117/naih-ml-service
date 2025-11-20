import torch
def classify_text_sync(model, tokenizer, text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    top = torch.argmax(probs, dim=1).item()
    confidence = probs[0][top].item()
    # Aquí debes mapear `top` a nombre de categoría (ej. via un archivo labels.json)
    category = f"label_{top}"
    return category, confidence
