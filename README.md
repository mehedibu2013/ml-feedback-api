# 🧠 Sentiment Analysis API with FastAPI

A simple FastAPI-based microservice that uses TextBlob to perform sentiment analysis on text input.

---

## 🚀 Features

- REST API using FastAPI
- Sentiment analysis with TextBlob
- JSON-based input/output

## 📁 Project Structure
```
ml-feedback-api/
├── app/
│   ├── main.py       # FastAPI routes and application entry point
│   ├── model.py      # Contains sentiment analysis logic (predict_sentiment function)
│   └── utils.py      # Helper functions used across the app
└── requirements.txt # List of Python dependencies needed to run the project
```

---

## 🚀 Getting Started

### 🔧 Installation (Local)

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/ml-feedback-api.git
   cd ml-feedback-api
2. Set up a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```
4. Run the server:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
5. Visit: http://127.0.0.1:8000/docs
6. Example Request
```
POST /predict
Request Body:
{
  "text": "I love this!"
}
Response:
{
  "sentiment": "positive"
}
```