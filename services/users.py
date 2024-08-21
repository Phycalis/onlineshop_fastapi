from api.schemas.schemas import UserSchema
from uow.unitofwork import IUnitOfWork


class UserService:

    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def add_user(self, user: UserSchema):
        user_dict = user.model_dump()
        async with self.uow:
            user_id = await self.uow.users.add_one(user_dict)
            await self.uow.commit()
            return user_id

    async def get_users(self):
        async with self.uow:
            users = await self.uow.users.find_all()
            return users