
from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

class Features(BaseModel):
    features: list

app = FastAPI()
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/predict")
def predict(data: Features):
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}
