from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict_sentiment

app = FastAPI()

class FeedbackInput(BaseModel):
    text: str

@app.post("/predict")
def predict(input: FeedbackInput):
    sentiment = predict_sentiment(input.text)
    return {"sentiment": sentiment}
