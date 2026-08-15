from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib

model = joblib.load('laptop_price_model.pkl')
model_columns = joblib.load('model_columns.pkl')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class LaptopSpecs(BaseModel):
    Company: str
    TypeName: str
    Inches: float
    Ram: int
    OpSys: str
    Weight: float
    SSD: int
    HDD: int
    Flash_Storage: int
    Hybrid: int
    Cpu_speed_GHz: float
    Cpu_brand: str
    Gpu_brand: str
    Touchscreen: int
    IPS: int
    PPI: float

@app.get("/")
def home():
    return {"message": "Laptop Price Predictor API is running"}

@app.post("/predict")
def predict_price(specs: LaptopSpecs):
    input_df = pd.DataFrame([specs.dict()])
    input_encoded = pd.get_dummies(input_df)
    input_final = input_encoded.reindex(columns=model_columns, fill_value=0)
    log_price = model.predict(input_final)[0]
    price = float(np.expm1(log_price))
    return {"predicted_price_euros": round(price, 2)}