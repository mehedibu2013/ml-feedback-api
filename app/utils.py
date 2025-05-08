from textblob import TextBlob

def clean_text(text: str) -> str:
    """Basic text cleaning."""
    return text.strip().replace("\n", " ").lower()

def analyze_sentiment(text: str) -> dict:
    """Returns both polarity and subjectivity."""
    blob = TextBlob(text)
    return {
        "polarity": blob.sentiment.polarity,
        "subjectivity": blob.sentiment.subjectivity
    }
