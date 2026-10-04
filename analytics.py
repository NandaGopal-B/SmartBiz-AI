from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from backend.database.connection import get_db
from backend.models import Customer, Product, Sale

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    customers = db.query(func.count(Customer.id)).scalar() or 0
    products = db.query(func.count(Product.id)).scalar() or 0
    orders = db.query(func.count(Sale.id)).scalar() or 0
    revenue = db.query(func.coalesce(func.sum(Sale.amount), 0)).scalar() or 0
    churn = db.query(func.coalesce(func.avg(Customer.churned), 0)).scalar() or 0
    return {
        "customers": customers,
        "products": products,
        "orders": orders,
        "revenue": round(float(revenue), 2),
        "churn_rate": round(float(churn) * 100, 2)
    }
