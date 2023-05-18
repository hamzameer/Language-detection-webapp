from fastapi import FastAPI
from pydantic import BaseModel 
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version
import uvicorn

app = FastAPI()

class TextIn(BaseModel):
    text: str
    
class PredictionOut(BaseModel):
    language: str

@app.get("/")
def home():
    return {'message': 'Ok!', 'version': f'{model_version}'}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}