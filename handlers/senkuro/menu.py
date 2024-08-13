import random

from aiogram import Router, types
from aiogram.filters import Command

from utils.senkuro import SenkuroApi

menu_router = Router()


@menu_router.message(Command("senkuro_menu"))
async def senkuro_menu(message: types.Message):
    await message.answer("You are in senkuro menu!")


@menu_router.message(Command("senkuro_getmanga"))
async def command_get_manga_handler(message: types.Message) -> None:
    manga_api = SenkuroApi()
    mangas_main_page = manga_api.get_main_page()
    if mangas_main_page is None:
        return None

    manga = random.choice(mangas_main_page.last_manga_chapters)
    await message.answer_photo(
        photo=manga.picture_url,
        caption=f"👉 <a href='{manga.page_url}'>{manga.title_ru}</a>",
    )
