from sqlalchemy import update, delete

from db.models import Cart
from repository.base_repository import Repository


class CartRepository(Repository):
    model = Cart

    async def plus_quantity(self, user_id, product_id):
        stmt = update(self.model).filter_by(user_id=user_id, product_id=product_id).values(
            quantity=self.model.quantity + 1
        ).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()

    async def minus_quantity(self, user_id, product_id):
        stmt = update(self.model).filter_by(user_id=user_id, product_id=product_id).values(
            quantity=self.model.quantity - 1
        ).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()

    async def delete_from_cart(self, user_id, product_id):
        stmt = delete(self.model).filter_by(user_id=user_id, product_id=product_id).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()
