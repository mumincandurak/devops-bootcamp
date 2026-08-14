from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    text: str = Field(min_length=1, max_length=500)


class PredictResponse(BaseModel):
    label: str
    score: float
