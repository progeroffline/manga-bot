import random
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from manga_api import SenkuroApi
from environs import Env

env = Env()
env.read_env()

TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
ADMIN_ID = env.int("ADMIN_ID")

bot = Bot(
    token=TELEGRAM_BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
    ),
)

manga_api = SenkuroApi()
dp = Dispatcher()


@dp.message(Command("getmanga"))
async def command_get_manga_handler(message: Message) -> None:
    mangas_main_page = manga_api.get_main_page()
    manga = random.choice(mangas_main_page["data"]["lastMangaChapters"]["edges"])
    manga = manga["node"]

    title = None

    for diff_title in manga["titles"]:
        if diff_title["lang"] == "RU":
            title = diff_title["content"]
    picture_url = manga["cover"]["original"]["url"]
    page_url = f"https://senkuro.com/manga/{manga['slug']}/chapters"

    await message.answer_photo(
        photo=picture_url, caption=f"👉 <a href='{page_url}'>{title}</a>"
    )


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    print(message)

    if message.from_user is None:
        return None

    await message.answer(
        text=f"Hello, @{message.from_user.username} {message.from_user.full_name}!"
    )

    if message.from_user.id == ADMIN_ID:
        return None
    if message.from_user.username == None:
        await bot.send_message(chat_id=ADMIN_ID, text=f"{message.from_user.id}")
    else:
        await bot.send_message(chat_id=ADMIN_ID, text=f"@{message.from_user.username}")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
