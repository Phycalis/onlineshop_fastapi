from fastapi import APIRouter, Depends

from api.schemas.schemas import ProductSchemaAdd, ProductSchema
from google_sheet_api.data import get_data_from_sheet, process_data
from services.products import ProductService
from uow.unitofwork import IUnitOfWork, UnitOfWork

router = APIRouter(prefix='/products',
                   tags=['Products'])


async def get_product_service(uow: IUnitOfWork = Depends(UnitOfWork)) -> ProductService:
    return ProductService(uow)


def get_data_from_excel():
    data = process_data(get_data_from_sheet())
    return data


@router.get('')
async def get_products(product_service: ProductService = Depends(get_product_service)):
    return await product_service.get_products()


@router.get('/hui')
async def get_products(category_id: int, product_service: ProductService = Depends(get_product_service)):
    return await product_service.get_product_by_category(category_id)


@router.get('/{product_id}')
async def get_product(product_id: int, product_service: ProductService = Depends(get_product_service)):
    return await product_service.get_product(product_id)


@router.post('')
async def create_product(product_data: ProductSchemaAdd,
                         product_service: ProductService = Depends(get_product_service)):
    return await product_service.add_product(product_data)


@router.post('/update')
async def update_product(product_id: int, product_data: ProductSchemaAdd,
                         product_service: ProductService = Depends(get_product_service)):
    return await product_service.update_product(product_id, product_data)


@router.post('/synchronize')
async def synchronize(product_service: ProductService = Depends(get_product_service),
                      data=Depends(get_data_from_excel)):
    return await product_service.excel_synchronize(data)
