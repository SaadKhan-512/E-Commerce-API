from pydantic import BaseModel, ConfigDict

## Schemas

# For adding a product
class Add_Product(BaseModel):
    name: str
    price: int
    stock_quantity: int

# for getting products
class Product_Response(BaseModel):
    model_config = ConfigDict(from_attributes=False)

    product_id: int
    name: str
    price: int
    stock_quantity: int

# For updaing a product
class Update_Product(BaseModel):
    id: int # Product id to update
    name: str
    price: int
    stock_quantity: int