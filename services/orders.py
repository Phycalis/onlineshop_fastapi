from api.schemas.schemas import OrderSchemaAdd
from uow.unitofwork import IUnitOfWork


class OrderService:

    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def add_order(self, order: OrderSchemaAdd):
        order_dict = order.model_dump()
        async with self.uow:
            order_id = await self.uow.orders.add_one(order_dict)
            await self.uow.commit()
            return order_id

    async def get_orders(self):
        async with self.uow:
            orders = await self.uow.orders.find_all()
            return orders