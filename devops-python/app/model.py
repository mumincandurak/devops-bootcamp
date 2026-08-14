import joblib
from pathlib import Path
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class DummyModel:
    POS = {"happy", "good", "great", "excellent"}
    NEG = {"sad", "bad", "terrible", "poor"}

    def predict_sentiment(self, text: str) -> dict:
        words = text.lower().split()
        p = sum(w in self.POS for w in words)
        n = sum(w in self.NEG for w in words)
        score = round((max(p, n) + 1) / (p + n + 2), 3)
        if p > n:
            return {"label": "positive", "score": score}
        elif n > p:
            return {"label": "negative", "score": score}
        else:
            return {"label": "neutral", "score": score}


def load_model() -> DummyModel:
    return DummyModel()


class MLSentimentModel:
    def __init__(self,pipeline):
        self.model = pipeline

    def predict_sentiment(self, text: str) -> dict:
        label = self.model.predict([text])[0]
        proba = self.model.predict_proba([text])[0]
        score = round(max(proba), 3)
        return {"label": label, "score": score}

def load_ml_model() -> MLSentimentModel:
    model_path = Path(__file__).parent / "model.joblib"
    pipeline = joblib.load(model_path)
    return MLSentimentModel(pipeline)