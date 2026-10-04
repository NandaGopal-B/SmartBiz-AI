from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, mean_absolute_error, r2_score
from ml.data_generator import generate_data

BASE = Path("ml/saved_models")
BASE.mkdir(parents=True, exist_ok=True)

def train():
    data_path = Path("data/processed/business_data.csv")
    data_path.parent.mkdir(parents=True, exist_ok=True)
    if not data_path.exists():
        generate_data().to_csv(data_path, index=False)
    df = pd.read_csv(data_path)

    churn_features = ["age", "annual_income", "total_spend", "purchase_frequency", "recency_days"]
    X = df[churn_features]
    y = df["churned"]
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.2, random_state=42, stratify=y)

    lr = Pipeline([("scale", StandardScaler()), ("model", LogisticRegression(max_iter=1000))])
    rf = Pipeline([("model", RandomForestClassifier(n_estimators=180, random_state=42))])
    lr.fit(Xtr, ytr)
    rf.fit(Xtr, ytr)

    lr_prob = lr.predict_proba(Xte)[:,1]
    rf_prob = rf.predict_proba(Xte)[:,1]
    metrics = {
        "logistic_regression": {
            "accuracy": round(accuracy_score(yte, lr.predict(Xte)), 4),
            "f1": round(f1_score(yte, lr.predict(Xte)), 4),
            "roc_auc": round(roc_auc_score(yte, lr_prob), 4)
        },
        "random_forest": {
            "accuracy": round(accuracy_score(yte, rf.predict(Xte)), 4),
            "f1": round(f1_score(yte, rf.predict(Xte)), 4),
            "roc_auc": round(roc_auc_score(yte, rf_prob), 4)
        }
    }
    joblib.dump(rf, BASE / "churn_model.joblib")

    sales_features = ["annual_income", "total_spend", "purchase_frequency", "recency_days", "quantity", "discount", "season"]
    X = df[sales_features]
    y = df["amount"]
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.2, random_state=42)
    reg = RandomForestRegressor(n_estimators=180, random_state=42)
    reg.fit(Xtr, ytr)
    pred = reg.predict(Xte)
    metrics["sales_regression"] = {
        "mae": round(mean_absolute_error(yte, pred), 2),
        "r2": round(r2_score(yte, pred), 4)
    }
    joblib.dump(reg, BASE / "sales_model.joblib")

    cluster_features = ["annual_income", "total_spend", "purchase_frequency", "recency_days"]
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[cluster_features])
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    labels = kmeans.fit_predict(scaled)
    df["segment"] = labels
    joblib.dump(scaler, BASE / "segment_scaler.joblib")
    joblib.dump(kmeans, BASE / "segment_model.joblib")
    df.to_csv(data_path, index=False)

    (BASE / "metrics.json").write_text(json.dumps(metrics, indent=2))
    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    train()
