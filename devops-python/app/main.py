from contextlib import asynccontextmanager
from fastapi import FastAPI , Depends , HTTPException
from app.config import settings
from app.model import load_ml_model, load_model
from app.schemas import PredictRequest, PredictResponse

ml = {}

def get_ml_model():
    if ml.get("ml") is None:
        raise HTTPException(status_code=503, detail="ML model not loaded")
    return ml["ml"]

def get_dummy_model():
    if ml.get("dummy") is None:
        raise HTTPException(status_code=503, detail="Dummy model not loaded")
    return ml["dummy"]

@asynccontextmanager
async def lifespan(app: FastAPI):
    ml["dummy"] = load_model()  # açılışta bir kez yükle
    ml["ml"] = load_ml_model()  # açılışta bir kez yükle
    yield  # servis burada çalışır
    ml.clear()  # kapanışta temizle


app = FastAPI(title=settings.app_name, lifespan=lifespan)


@app.post("/models/predict", response_model=PredictResponse)
def predict( request: PredictRequest, model = Depends(get_dummy_model), verbose: bool = False):
    result = model.predict_sentiment(request.text)
    if verbose:
        print(f" input={request.text!r} -> {result}")
    return PredictResponse(label=result["label"], score=result["score"])

@app.post("/models/sentiment", response_model=PredictResponse)
def sentiment(request: PredictRequest, model = Depends(get_ml_model), verbose: bool = False):
    result = model.predict_sentiment(request.text)
    if verbose:
        print(f" input={request.text!r} -> {result}")
    return PredictResponse(label=result["label"], score=result["score"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
