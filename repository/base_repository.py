from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas.schemas import ProductSchemaAdd


class AbstractRepository(ABC):
    @abstractmethod
    def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    def find_all(self):
        raise NotImplementedError

    @abstractmethod
    def find_one(self, data_id: int):
        raise NotImplementedError

    @abstractmethod
    def update_one(self, data_id: int, data: dict):
        raise NotImplementedError


class Repository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()

    async def find_all(self):
        result = await self.session.execute(select(self.model))
        result = [row[0].to_read_model() for row in result.all()]
        return result

    async def find_one(self, data_id: int):
        query = select(self.model).filter_by(id=data_id)
        result = await self.session.execute(query)
        result = [row[0].to_read_model() for row in result]
        return result

    async def update_one(self, data_id: int, data: ProductSchemaAdd):
        stmt = update(self.model).filter_by(id=data_id).values(
            title=data.title,
            description=data.description,
            price=data.price, image=data.image,
            category_id=data.category_id,
            file_id=data.file_id
        ).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()

    async def delete_one(self, data_id: int):
        stmt = delete(self.model).filter_by(id=data_id).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()
