from fastapi import APIRouter, Depends

from api.schemas.schemas import OrderSchemaAdd
from services.orders import OrderService
from uow.unitofwork import IUnitOfWork, UnitOfWork

router = APIRouter(prefix='/orders',
                   tags=['Orders'])


async def get_order_service(uow: IUnitOfWork = Depends(UnitOfWork)) -> OrderService:
    return OrderService(uow)


@router.get('')
async def get_orders(order_service: OrderService = Depends(get_order_service)):
    return await order_service.get_orders()


@router.post('')
async def create_order(order_data: OrderSchemaAdd,
                       order_service: OrderService = Depends(get_order_service)):
    return await order_service.add_order(order_data)
