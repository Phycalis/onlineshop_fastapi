from abc import ABC, abstractmethod

from db.database import async_session_maker
from repository.cart_repository import CartRepository
from repository.category_repository import CategoryRepository
from repository.order_repository import OrderRepository
from repository.product_repository import ProductRepository
from repository.user_repository import UserRepository


class IUnitOfWork(ABC):

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork(IUnitOfWork):

    def __init__(self):
        self.factory_session = async_session_maker

    async def __aenter__(self):
        self.session = self.factory_session()
        self.products = ProductRepository(self.session)
        self.orders = OrderRepository(self.session)
        self.users = UserRepository(self.session)
        self.categories = CategoryRepository(self.session)
        self.carts = CartRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
