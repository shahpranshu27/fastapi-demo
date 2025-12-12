from fastapi import FastAPI, Depends
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Hello from Inventory Trac!"

products = [
    Product(id=1, name="Product A", description="Description A", price=10.0, quantity=100),
    Product(id=2, name="Product B", description="Description B", price=20.0, quantity=200),
    Product(id=3, name="Product C", description="Description C", price=30.0, quantity=300),
]

def init_db():
    db = session()
    
    count = db.query(database_models.Product).count()
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump())) # Converting the pydantic type product to the sqlalchemy Base type Product
        db.commit()
        
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    
    db_products = db.query(database_models.Product).all()
    
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    
    if db_product:
        return db_product

    return "product not found"

@app.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product


@app.put("/product")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return product
    else:
        return "product not found"

@app.delete("/product")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product deleted"
    else:
        return "product not found"