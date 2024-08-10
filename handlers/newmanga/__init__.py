from aiogram import Router
from .menu import menu_router

newmanga_router = Router()
newmanga_router.include_routers(
    menu_router,
)
