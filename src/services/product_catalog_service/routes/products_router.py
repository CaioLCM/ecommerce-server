from fastapi import APIRouter
from pydantic import BaseModel

products_router = APIRouter()

class Product(BaseModel):
    name: str
    price: float

@products_router.post("/")
def create_product(product: Product):
    return {"message": "Creating product"}