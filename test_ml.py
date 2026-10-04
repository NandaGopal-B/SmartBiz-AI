from ml.data_generator import generate_data

def test_generated_data_shape():
    df = generate_data(100)
    assert len(df) == 100
    assert "annual_income" in df.columns
    assert "churned" in df.columns
    assert "amount" in df.columns
