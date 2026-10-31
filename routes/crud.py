from fastapi import APIRouter, Depends, HTTPException, status, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pathlib import Path
from database import database, models
import schemas

# __file__ -> Current file, .parent -> routes and so on(.parent.parent.....)
BASE_DIR = Path(__file__).resolve().parent.parent

# To connect python with HTML
templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)
# main app
router = APIRouter(tags=["CRUD"])

# Dashboard
@router.get("/dashboard")
def dashboard(request: Request, db: Session = Depends(database.get_db)):
    products = db.query(models.Product).order_by(models.Product.product_id).all()

    return templates.TemplateResponse(
        request=request,
        name="admin_roles.html",
        context={"name": "Saad", "products": products}
    )

# Get items
@router.get("/items")
def get_items(request: Request, db: Session = Depends(database.get_db)):
    products = db.query(models.Product).order_by(models.Product.product_id).all()

    return templates.TemplateResponse(
        request=request,
        name="items.html",
        context={"name": "Saad", "products": products}
    )

# Add item
# Load File:
@router.get("/items/add")
def add_item_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="add_item.html",
        context={}
    )

# 
@router.post("/items/add")
def add_item(
    request: Request, 
    db: Session = Depends(database.get_db),
    name: str = Form(...),
    price: float = Form(...),
    stock: int = Form(...)):

    obj = models.Product(**{"name": name, "price": price, "stock_quantity": stock})
    db.add(obj)
    db.commit()

    return templates.TemplateResponse(
        request=request,
        name="add_item.html",
        context={"products": "products"}
    )

# # Get all products
# @router.get("", response_model=list[schemas.Product_Response])
# def get_products(db: Session = Depends(database.get_db)):
#     products = db.query(models.Product).order_by(models.Product.product_id).all()
#     return products

# # Add a product to database
# @router.post("")
# def add_products(product: schemas.Add_Product, db: Session = Depends(database.get_db)):
#     product_obj = models.Product(**product.dict())

#     db.add(product_obj)
#     db.commit()
#     db.refresh(product_obj)

#     return product_obj

# # Update an existing product
# @router.put("")
# def update_product(updated_product: schemas.Update_Product, db: Session = Depends(database.get_db)):
#     product = db.query(models.Product).filter(models.Product.product_id == updated_product.id).first()

#     # If product was not found:
#     if not product:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, 
#             detail=f"Product with id of {updated_product.id} was not found in database."
#         )

#     # Else Update the existing product(Given by user)
#     product.name = updated_product.name
#     product.price = updated_product.price
#     product.stock_quantity = updated_product.stock_quantity

#     db.commit()

#     return {"message": "Product updated successfully."}

# # Deleting a product
# @router.delete("")
# def delete(id: int, db: Session = Depends(database.get_db)):
#     product = db.query(models.Product).filter(models.Product.product_id == id).first()

#     # If product was not found:
#     if not product:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, 
#             detail=f"Product with id of {id} was not found in database."
#         )
    
#     # Else delete that product
#     db.delete(product)
#     db.commit()

#     return {"message": f"Product with id of {id} has been deleted successfully."}