# SmartBiz AI — Full-Stack Business Intelligence & ML Platform

SmartBiz AI is an end-to-end business intelligence platform built with Python, FastAPI, MySQL, HTML/CSS/JavaScript, Streamlit, Plotly, Pandas, NumPy and Scikit-learn.

## Highlights

- REST API with FastAPI
- MySQL-ready relational schema
- Customer, product and sales CRUD APIs
- Dashboard frontend using HTML/CSS/JavaScript
- Streamlit analytics dashboard
- Customer churn prediction
- K-Means customer segmentation
- Sales prediction
- Model evaluation and feature importance
- Synthetic business dataset for demonstration
- Automated tests
- Environment-variable configuration
- GitHub-ready project structure

## Architecture

```text
HTML/CSS/JavaScript
        |
        v
     FastAPI
        |
   +----+----+
   |         |
 MySQL      ML
 Database   Engine
             |
      +------+------+ 
      |      |      |
    Churn  Sales  K-Means
             |
             v
        Streamlit
        Analytics
```

## Project Structure

```text
smartbiz-ai/
├── backend/
│   ├── api/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   └── main.py
├── frontend/
├── ml/
├── dashboard/
├── notebooks/
├── data/
├── tests/
├── docs/
├── requirements.txt
├── .env.example
└── README.md
```

## Quick Start

### 1. Create an environment

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment

Copy `.env.example` to `.env` and edit the values.

The application defaults to SQLite for zero-configuration local demonstration. Set `DATABASE_URL` to a MySQL connection string when MySQL is available.

### 4. Generate demo data and train models

```bash
python -m ml.train_all
```

This creates:

- `data/processed/business_data.csv`
- trained model files in `ml/saved_models/`
- `ml/saved_models/metrics.json`

### 5. Start FastAPI

```bash
uvicorn backend.main:app --reload
```

Open:

- API: http://127.0.0.1:8000
- Swagger docs: http://127.0.0.1:8000/docs

### 6. Start frontend

The frontend is served directly by FastAPI at:

http://127.0.0.1:8000/

### 7. Start Streamlit

In another terminal:

```bash
streamlit run dashboard/app.py
```

## MySQL Setup

Create a database:

```sql
CREATE DATABASE smartbiz;
```

Then set:

```env
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/smartbiz
```

Run:

```bash
python -m backend.database.seed
```

## ML Modules

### Customer Churn
Binary classification predicting whether a customer is likely to churn.

Models:
- Logistic Regression
- Random Forest

### Customer Segmentation
K-Means clustering based on:
- annual income
- total spend
- purchase frequency
- recency

### Sales Prediction
Random Forest regression predicting sales amount from business/customer attributes.

## Testing

```bash
pytest -q
```

## API Endpoints

```text
GET    /api/health
GET    /api/customers
POST   /api/customers
GET    /api/customers/{id}
GET    /api/products
POST   /api/products
GET    /api/sales
POST   /api/sales
GET    /api/analytics/summary
POST   /api/ml/churn
POST   /api/ml/sales-prediction
GET    /api/ml/segments
```

## Academic / Portfolio Value

This project demonstrates:

- Python programming
- SQL and relational database design
- Data cleaning and feature engineering
- Exploratory data analysis
- Machine learning
- Classification
- Regression
- Clustering
- REST API development
- Frontend development
- Data visualization
- Testing
- Git/GitHub project organization

## Disclaimer

The included dataset is synthetic and generated solely for demonstration and portfolio purposes. Replace it with an approved real dataset if your institution requires original data collection.
