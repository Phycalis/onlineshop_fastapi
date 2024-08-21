from fastapi import APIRouter, Depends

from api.schemas.schemas import UserSchemaAdd, UserSchema
from services.users import UserService
from uow.unitofwork import IUnitOfWork, UnitOfWork

router = APIRouter(prefix='/users',
                   tags=['Users'])


async def get_user_service(uow: IUnitOfWork = Depends(UnitOfWork)) -> UserService:
    return UserService(uow)


@router.get('')
async def get_users(user_service: UserService = Depends(get_user_service)):
    return await user_service.get_users()


@router.post('')
async def create_user(user_data: UserSchema,
                      user_service: UserService = Depends(get_user_service)):
    return await user_service.add_user(user_data)
