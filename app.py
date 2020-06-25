from loader import bot, create_db
import asyncio


async def on_startup(dp):
    from utils import on_startup_notify
    await asyncio.sleep(10)
    await create_db()
    await on_startup_notify(dp)


async def on_shutdown(dp):
    await bot.close()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
