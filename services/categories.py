from api.schemas.schemas import CategorySchemaAdd
from uow.unitofwork import IUnitOfWork


class CategoryService:

    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def add_category(self, categories: CategorySchemaAdd):
        categories_dicts = categories.model_dump()
        async with self.uow:
            categories = await self.uow.categories.add_one(categories_dicts)
            await self.uow.commit()
            return categories

    async def get_categories(self):
        async with self.uow:
            categories = await self.uow.categories.find_all()
            return categories
