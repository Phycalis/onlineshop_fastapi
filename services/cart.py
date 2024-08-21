from api.schemas.schemas import CartSchemaAdd
from uow.unitofwork import IUnitOfWork


class CartService:

    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def new_cart(self, cart: CartSchemaAdd):
        cart_dict = cart.model_dump()
        async with self.uow:
            cart_id = await self.uow.carts.add_one(cart_dict)
            await self.uow.commit()
            return cart_id

    async def get_cart(self, user_id: int):
        async with self.uow:
            cart = await self.uow.carts.find_one(user_id)
            return cart

    async def delete_cart(self, user_id, product_id):
        async with self.uow:
            cart = await self.uow.carts.delete_from_cart(user_id=user_id, product_id=product_id)
            await self.uow.commit()
            return cart

    async def increase_quantity(self, user_id, product_id):
        async with self.uow:
            cart = await self.uow.carts.plus_quantity(user_id=user_id, product_id=product_id)
            await self.uow.commit()
            return cart

    async def decrease_quantity(self, user_id, product_id):
        async with self.uow:
            cart = await self.uow.carts.minus_quantity(user_id=user_id, product_id=product_id)
            await self.uow.commit()
            return cart

