from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import database, models
import schemas

router = APIRouter(prefix="/products")

# Get all products
@router.get("", response_model=list[schemas.Product_Response])
def get_products(db: Session = Depends(database.get_db)):
    products = db.query(models.Product).order_by(models.Product.product_id).all()
    return products

# Add a product to database
@router.post("")
def add_products(product: schemas.Add_Product, db: Session = Depends(database.get_db)):
    product_obj = models.Product(**product.dict())

    db.add(product_obj)
    db.commit()
    db.refresh(product_obj)

    return product_obj

# Update an existing product
@router.put("")
def update_product(updated_product: schemas.Update_Product, db: Session = Depends(database.get_db)):
    product = db.query(models.Product).filter(models.Product.product_id == updated_product.id).first()

    # If product was not found:
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Product with id of {updated_product.id} was not found in database."
        )

    # Else Update the existing product(Given by user)
    product.name = updated_product.name
    product.price = updated_product.price
    product.stock_quantity = updated_product.stock_quantity

    db.commit()

    return {"message": "Product updated successfully."}
