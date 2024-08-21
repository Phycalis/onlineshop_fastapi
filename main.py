from fastapi import FastAPI

from api.endpoints.products import router as product_router
from api.endpoints.orders import router as order_router
from api.endpoints.users import router as user_router
from api.endpoints.categories import router as category_router
from api.endpoints.cart import router as cart_router

app = FastAPI()

app.include_router(product_router)
app.include_router(order_router)
app.include_router(user_router)
app.include_router(category_router)
app.include_router(cart_router)
