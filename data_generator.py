from pathlib import Path
import numpy as np
import pandas as pd

def generate_data(n=1500, seed=42):
    rng = np.random.default_rng(seed)
    cities = ["Hyderabad", "Bengaluru", "Chennai", "Mumbai", "Delhi", "Pune", "Vizag", "Kolkata"]
    genders = ["Male", "Female", "Other"]
    regions = ["North", "South", "East", "West", "Central"]
    categories = ["Electronics", "Home", "Fashion", "Grocery", "Sports"]

    age = rng.integers(18, 65, n)
    income = np.maximum(18000, rng.normal(85000, 35000, n))
    freq = rng.poisson(7, n) + 1
    recency = rng.integers(1, 180, n)
    spend = np.maximum(500, income * rng.uniform(0.08, 0.45, n) * (freq / 8))
    churn_prob = 1 / (1 + np.exp(-(0.012 * recency - 0.18 * freq + 0.3)))
    churned = rng.random(n) < churn_prob

    quantity = rng.integers(1, 8, n)
    discount = rng.uniform(0, 0.30, n)
    season = rng.integers(1, 5, n)
    base = 800 + income * 0.012 + freq * 110 + quantity * 180
    amount = np.maximum(100, base * (1 - discount) + rng.normal(0, 250, n))

    df = pd.DataFrame({
        "customer_name": [f"Customer {i+1:04d}" for i in range(n)],
        "age": age,
        "gender": rng.choice(genders, n),
        "city": rng.choice(cities, n),
        "region": rng.choice(regions, n),
        "annual_income": np.round(income, 2),
        "total_spend": np.round(spend, 2),
        "purchase_frequency": freq,
        "recency_days": recency,
        "churned": churned.astype(int),
        "quantity": quantity,
        "discount": np.round(discount, 3),
        "season": season,
        "amount": np.round(amount, 2),
        "category": rng.choice(categories, n),
    })
    return df

if __name__ == "__main__":
    out = Path("data/processed/business_data.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    generate_data().to_csv(out, index=False)
    print(f"Created {out}")
