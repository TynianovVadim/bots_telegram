from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from utils.db_api import DBCommands
from loader import dp


database = DBCommands()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')

    referral = message.get_args()
    id = await database.add_new_user(referral=referral)

    text = ""
    if not id:
        id = await database.get_id()
    else:
        text += "Пользователь записан в БД"

    await message.answer(text)
