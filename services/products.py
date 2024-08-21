from api.schemas.schemas import ProductSchemaAdd, ProductSchema
from uow.unitofwork import IUnitOfWork


class ProductService:

    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def add_product(self, products: ProductSchemaAdd):
        products_dicts = products.model_dump()
        async with self.uow:
            product_id = await self.uow.products.add_one(products_dicts)
            await self.uow.commit()
            return product_id

    async def get_product(self, product_id: int):
        async with self.uow:
            products = await self.uow.products.find_one(product_id)
            return products

    async def get_products(self):
        async with self.uow:
            products = await self.uow.products.find_all()
            return products

    async def update_product(self, product_id: int, products: ProductSchemaAdd):
        async with self.uow:
            products = await self.uow.products.update_one(product_id, products)
            await self.uow.commit()
            return products

    async def get_product_by_category(self, category_id: int):
        async with self.uow:
            products = await self.uow.products.get_products_by_category(category_id)
            return products

    async def excel_synchronize(self, from_excel: list):
        async with self.uow:
            await self.uow.products.excel_synchronize(from_excel)
            await self.uow.commit()
            return {"status": 201, "message": "data synchronized successfully"}
