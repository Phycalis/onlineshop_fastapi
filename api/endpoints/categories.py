from fastapi import APIRouter, Depends

from api.schemas.schemas import CategorySchemaAdd
from google_sheet_api.data import process_data, get_data_from_sheet
from services.categories import CategoryService
from uow.unitofwork import IUnitOfWork, UnitOfWork

router = APIRouter(prefix='/categories',
                   tags=['Categories'])


async def get_product_service(uow: IUnitOfWork = Depends(UnitOfWork)) -> CategoryService:
    return CategoryService(uow)


def get_data_from_excel():
    data = process_data(get_data_from_sheet())
    return data


@router.get('')
async def get_products(category_service: CategoryService = Depends(get_product_service)):
    return await category_service.get_categories()


@router.post('')
async def create_product(category_data: CategorySchemaAdd,
                         category_service: CategoryService = Depends(get_product_service)):
    return await category_service.add_category(category_data)
