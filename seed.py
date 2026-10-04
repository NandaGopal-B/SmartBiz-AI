import pandas as pd
from backend.database.connection import Base, engine, SessionLocal
from backend.models import Customer, Product, Sale

def seed():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    df = pd.read_csv("data/processed/business_data.csv")

    customers = []
    for i, r in df.head(500).iterrows():
        customers.append(Customer(
            name=r["customer_name"], age=int(r["age"]), gender=r["gender"],
            city=r["city"], annual_income=float(r["annual_income"]),
            total_spend=float(r["total_spend"]),
            purchase_frequency=int(r["purchase_frequency"]),
            recency_days=int(r["recency_days"]), churned=bool(r["churned"])
        ))
    db.add_all(customers)

    categories = ["Electronics", "Home", "Fashion", "Grocery", "Sports"]
    products = []
    for i, category in enumerate(categories, 1):
        products.extend([
            Product(name=f"{category} Pro", category=category, price=799+i*250, stock=100+i*25),
            Product(name=f"{category} Essential", category=category, price=399+i*120, stock=150+i*20),
        ])
    db.add_all(products)
    db.commit()

    for i, r in df.head(500).iterrows():
        db.add(Sale(
            customer_id=int(i)+1,
            product_id=(int(i) % 10)+1,
            quantity=int(r["quantity"]),
            amount=float(r["amount"]),
            region=r["region"],
            sale_month=int((int(i) % 12)+1)
        ))
    db.commit()
    db.close()

if __name__ == "__main__":
    seed()
    print("Demo database seeded successfully.")

