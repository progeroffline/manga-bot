import random

from aiogram import Router, types
from aiogram.filters import Command

from utils.newmanga import NewMangaApi

menu_router = Router()


@menu_router.message(Command("newmanga_menu"))
async def new_manga_menu(message: types.Message):
    await message.answer("You are in new manga menu!")


@menu_router.message(Command("newmanga_getmanga"))
async def command_get_new_manga_handler(message: types.Message) -> None:
    manga_api = NewMangaApi()
    mangas_main_page = manga_api.get_main_page()
    if mangas_main_page is None:
        return

    manga = random.choice(mangas_main_page.items)
    await message.answer_photo(
        photo=manga.picture_url,
        caption=f"👉 <a href='{manga.page_url}'>{manga.title_ru}</a>",
    )
