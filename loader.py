import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from data.config import TELEGRAM_BOT_TOKEN
from logzero import logfile, logger

if not os.path.exists("logs/"):
    os.system("mkdir logs")
logfile("logs/bot.log")


bot = Bot(
    token=TELEGRAM_BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
    ),
)

storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
