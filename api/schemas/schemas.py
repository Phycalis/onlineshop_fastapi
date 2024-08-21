import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    id: int
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class UserSchemaAdd(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    phone: str


class ProductSchema(BaseModel):
    id: int
    title: str
    description: str
    price: float
    image: Optional[str] = None
    category_id: Optional[int] = None
    file_id: Optional[str] = None


class ProductSchemaAdd(BaseModel):
    title: str
    description: str
    price: float
    image: Optional[str] = None
    category_id: Optional[int] = None
    file_id: Optional[str] = None


class OrderSchemaAdd(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    created_at: datetime.datetime = Field(default=datetime.datetime.utcnow())


class OrderSchema(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    created_at: datetime.datetime = Field(default=datetime.datetime.utcnow())


class CategorySchema(BaseModel):
    id: int
    name: str


class CategorySchemaAdd(BaseModel):
    name: str


class CartSchema(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int


class CartSchemaAdd(BaseModel):
    user_id: int
    product_id: int
    quantity: int
