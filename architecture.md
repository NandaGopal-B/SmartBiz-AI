# Architecture

## Layers

### Presentation
- HTML
- CSS
- JavaScript
- Streamlit

### Application
- FastAPI
- Pydantic
- REST endpoints

### Data
- SQLAlchemy
- MySQL
- SQLite development fallback

### Intelligence
- Pandas
- NumPy
- Scikit-learn
- Random Forest
- Logistic Regression
- K-Means

## Data Flow

```text
User → Frontend → FastAPI → Database
                     |
                     └→ ML Services → Prediction
                                      |
                                  Dashboard
```
