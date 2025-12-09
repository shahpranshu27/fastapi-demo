from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Hello from Inventory Trac!"

products = [
    Product(id=1, name="Product A", description="Description A", price=10.0, quantity=100),
    Product(id=2, name="Product B", description="Description B", price=20.0, quantity=200),
    Product(id=3, name="Product C", description="Description C", price=30.0, quantity=300),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product

    return "product not found"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product