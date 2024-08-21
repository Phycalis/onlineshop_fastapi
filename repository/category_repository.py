from db.models import Category
from repository.base_repository import Repository


class CategoryRepository(Repository):
    model = Category
