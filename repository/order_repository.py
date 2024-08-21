from db.models import Order
from repository.base_repository import Repository


class OrderRepository(Repository):
    model = Order
