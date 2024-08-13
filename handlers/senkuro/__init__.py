from aiogram import Router
from .menu import menu_router

senkuro_router = Router()
senkuro_router.include_routers(
    menu_router,
)
