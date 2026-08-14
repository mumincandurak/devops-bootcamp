import joblib
from pathlib import Path
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


if __name__ == "__main__":
    # Örnek eğitim verisi
    texts = ["this is a great day", "this is a terrible day", "just an ordinary day"]
    labels = ["positive", "negative", "neutral"]

    model = make_pipeline(TfidfVectorizer(), LogisticRegression())
    model.fit(texts, labels)

    # Modeli kaydet
    model_path = Path(__file__).parent / "model.joblib"
    joblib.dump(model, model_path)