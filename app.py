import asyncio

from handlers import start_router, newmanga_router, senkuro_router
from loader import bot, dp
from middlewares import UpdateLoggerMiddleware


async def on_startup():
    dp.update.outer_middleware(UpdateLoggerMiddleware())

    dp.include_routers(start_router, newmanga_router, senkuro_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(on_startup())
