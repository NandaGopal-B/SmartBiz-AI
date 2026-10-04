from pydantic import BaseModel, ConfigDict

class CustomerBase(BaseModel):
    name: str
    age: int
    gender: str
    city: str
    annual_income: float
    total_spend: float = 0
    purchase_frequency: int = 0
    recency_days: int = 0
    churned: bool = False

class CustomerCreate(CustomerBase):
    pass

class CustomerOut(CustomerBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class ProductBase(BaseModel):
    name: str
    category: str
    price: float
    stock: int = 0

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class SaleBase(BaseModel):
    customer_id: int
    product_id: int
    quantity: int
    amount: float
    region: str
    sale_month: int

class SaleCreate(SaleBase):
    pass

class SaleOut(SaleBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
