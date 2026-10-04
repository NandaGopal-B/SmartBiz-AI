from pathlib import Path
import joblib
import pandas as pd

BASE = Path(__file__).resolve().parent / "saved_models"

def ensure_models():
    if not (BASE / "churn_model.joblib").exists():
        from ml.train_all import train
        train()

def predict_churn(data):
    ensure_models()
    model = joblib.load(BASE / "churn_model.joblib")
    X = pd.DataFrame([data])
    probability = float(model.predict_proba(X)[0, 1])
    return {
        "churn_probability": round(probability, 4),
        "risk": "High" if probability >= .65 else "Medium" if probability >= .35 else "Low"
    }

def predict_sales(data):
    ensure_models()
    model = joblib.load(BASE / "sales_model.joblib")
    X = pd.DataFrame([data])
    prediction = float(model.predict(X)[0])
    return {"predicted_sales": round(max(0, prediction), 2)}

def get_segments():
    ensure_models()
    df = pd.read_csv("data/processed/business_data.csv")
    counts = df["segment"].value_counts().sort_index()
    return [{"segment": int(k), "customers": int(v)} for k, v in counts.items()]
