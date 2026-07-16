from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob
from deep_translator import GoogleTranslator

app = FastAPI(title="YZ Projesi")

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "Sistem çalışıyor", "version": "1.0.0"}

@app.post("/predict")
def predict_sentiment(request: TextRequest):
    try:
        translated_text = GoogleTranslator(source='auto', target='en').translate(request.text)
    except Exception:
        translated_text = request.text

    analysis = TextBlob(translated_text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        sentiment = "Pozitif"
    elif polarity < -0.1:
        sentiment = "Negatif"
    else:
        sentiment = "Nötr"

    return {
        "text": request.text,
        "translated_text": translated_text,
        "sentiment": sentiment,
        "score": round(polarity, 2)
    }