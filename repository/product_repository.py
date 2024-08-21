from sqlalchemy import insert, select

from db.models import Product
from repository.base_repository import Repository


class ProductRepository(Repository):
    model = Product

    async def get_products_by_category(self, category_id: int):
        query = select(self.model).filter_by(category_id=category_id)
        res = await self.session.execute(query)
        res = [row[0].to_read_model() for row in res]
        return res

    async def excel_synchronize(self, from_excel: list):
        res = None
        for data in from_excel:
            stmt = insert(self.model).values(title=data['Наименование'],
                                             description=data['Артикул'],
                                             price=float(data['Себест-ть, руб.'].replace(',', '.')),
                                             image=data['Поставщик'].encode('utf-8')).returning(self.model)
            res = await self.session.execute(stmt)
        if res:
            return res.scalar_one().to_read_model()
        else:
            print('No data found')
