from fastapi import APIRouter
from pydantic import BaseModel
from ml.predict import predict_churn, predict_sales, get_segments

router = APIRouter(prefix="/ml", tags=["Machine Learning"])

class ChurnInput(BaseModel):
    age: float
    annual_income: float
    total_spend: float
    purchase_frequency: float
    recency_days: float

class SalesInput(BaseModel):
    annual_income: float
    total_spend: float
    purchase_frequency: float
    recency_days: float
    quantity: float
    discount: float
    season: float

@router.post("/churn")
def churn(payload: ChurnInput):
    return predict_churn(payload.model_dump())

@router.post("/sales-prediction")
def sales_prediction(payload: SalesInput):
    return predict_sales(payload.model_dump())

@router.get("/segments")
def segments():
    return get_segments()
