from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

start_router = Router()


@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if message.from_user is None:
        return None

    await message.answer(
        text=f"Hello, @{message.from_user.username} {message.from_user.full_name}!"
    )
