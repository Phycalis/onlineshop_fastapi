from fastapi import APIRouter, Depends

from api.schemas.schemas import CartSchemaAdd
from services.cart import CartService
from uow.unitofwork import IUnitOfWork, UnitOfWork

router = APIRouter(prefix='/cart',
                   tags=['Cart'])


async def get_cart_service(uow: IUnitOfWork = Depends(UnitOfWork)) -> CartService:
    return CartService(uow)


@router.get('')
async def get_user_cart(user_id: int, cart_service: CartService = Depends(get_cart_service)):
    return await cart_service.get_cart(user_id)


@router.post('')
async def create_user_cart(cart_data: CartSchemaAdd,
                           cart_service: CartService = Depends(get_cart_service)):
    return await cart_service.new_cart(cart_data)


@router.post('/increase_quantity')
async def increase_quantity(user_id: int, product_id: int,
                            cart_service: CartService = Depends(get_cart_service)):
    return await cart_service.increase_quantity(user_id, product_id)


@router.post('/decrease_quantity')
async def decrease_quantity(user_id: int, product_id: int,
                            cart_service: CartService = Depends(get_cart_service)):
    return await cart_service.decrease_quantity(user_id, product_id)


@router.delete('/delete')
async def delete_cart(user_id: int, product_id: int,
                      cart_service: CartService = Depends(get_cart_service)):
    return await cart_service.delete_cart(user_id, product_id)
