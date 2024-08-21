import datetime

from sqlalchemy import text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.schemas.schemas import ProductSchema, OrderSchema, UserSchema, CategorySchema, CartSchema

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    address: Mapped[str] = mapped_column(nullable=True)

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            name=self.name,
            email=self.email,
            phone=self.phone,
            address=self.address
        )


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    def to_read_model(self) -> CategorySchema:
        return CategorySchema(
            id=self.id,
            name=self.name,
        )


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    price: Mapped[float]
    image: Mapped[str] = mapped_column(nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=True)
    category: Mapped["Category"] = relationship(Category, lazy='joined')
    file_id: Mapped[str] = mapped_column(nullable=True)

    def to_read_model(self) -> ProductSchema:
        return ProductSchema(
            id=self.id,
            title=self.title,
            description=self.description,
            price=self.price,
            image=self.image,
            category_id=self.category_id,
            file_id=self.file_id
        )


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))

    def to_read_model(self) -> OrderSchema:
        return OrderSchema(
            id=self.id,
            user_id=self.user_id,
            product_id=self.product_id,
            quantity=self.quantity,
            created_at=self.created_at
        )


class Cart(Base):
    __tablename__ = 'cart'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int]

    def to_read_model(self) -> CartSchema:
        return CartSchema(
            id=self.id,
            user_id=self.user_id,
            product_id=self.product_id,
            quantity=self.quantity,
        )
