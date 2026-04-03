import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")


def get_request(endpoint, params=None):
    try:
        response = requests.get(endpoint, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None


def post_request(endpoint, json_payload):
    try:
        response = requests.post(endpoint, json=json_payload, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None


def analyze_review_sentiments(text):
    if not text:
        return {"sentiment": "neutral"}
    try:
        request_url = sentiment_analyzer_url.rstrip('/') + '/analyze/' + requests.utils.quote(text)
        response = requests.get(request_url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception:
        try:
            import nltk
            from nltk.sentiment import SentimentIntensityAnalyzer
            try:
                sia = SentimentIntensityAnalyzer()
            except LookupError:
                nltk.download('vader_lexicon')
                sia = SentimentIntensityAnalyzer()
            scores = sia.polarity_scores(text)
            pos = scores['pos']
            neg = scores['neg']
            neu = scores['neu']
            sentiment = 'positive'
            if neg > pos and neg > neu:
                sentiment = 'negative'
            elif neu > neg and neu > pos:
                sentiment = 'neutral'
            return {"sentiment": sentiment}
        except Exception:
            return {"sentiment": "neutral"}
