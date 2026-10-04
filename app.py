import json
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="SmartBiz AI", page_icon="📊", layout="wide")

DATA = Path("data/processed/business_data.csv")
if not DATA.exists():
    from ml.data_generator import generate_data
    DATA.parent.mkdir(parents=True, exist_ok=True)
    generate_data().to_csv(DATA, index=False)

df = pd.read_csv(DATA)

st.title("📊 SmartBiz AI")
st.caption("Full-Stack Business Intelligence & Machine Learning Platform")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Customers", f"{len(df):,}")
c2.metric("Revenue", f"₹{df['amount'].sum():,.0f}")
c3.metric("Avg. Order", f"₹{df['amount'].mean():,.0f}")
c4.metric("Churn Rate", f"{df['churned'].mean()*100:.1f}%")

st.divider()

left, right = st.columns(2)
with left:
    st.subheader("Revenue by Region")
    region = df.groupby("region", as_index=False)["amount"].sum()
    st.plotly_chart(px.bar(region, x="region", y="amount", title="Revenue by Region"), use_container_width=True)

with right:
    st.subheader("Customer Segments")
    if "segment" in df:
        seg = df["segment"].value_counts().reset_index()
        seg.columns = ["segment", "customers"]
        st.plotly_chart(px.pie(seg, names="segment", values="customers", hole=.45), use_container_width=True)

st.subheader("Income vs Total Spend")
st.plotly_chart(
    px.scatter(df, x="annual_income", y="total_spend", size="purchase_frequency",
               color="churned", hover_data=["city", "gender"],
               title="Customer Value Analysis"),
    use_container_width=True
)

st.subheader("Model Performance")
metrics_file = Path("ml/saved_models/metrics.json")
if metrics_file.exists():
    metrics = json.loads(metrics_file.read_text())
    st.json(metrics)
else:
    st.info("Run `python -m ml.train_all` to generate model metrics.")

with st.expander("Data Preview"):
    st.dataframe(df.head(100), use_container_width=True)
