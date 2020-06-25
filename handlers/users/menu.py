from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu

from loader import dp, bot
from utils.db_api import DBCommands
from utils.misc import rate_limit

import random


database = DBCommands()


@rate_limit(5, "menu")
@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Choose your favorite food, please.", reply_markup=menu)


@dp.message_handler(Text("Мой баланс"))
async def check_user_balance(message: Message):
    balance = await database.check_balance()
    text = f"Ваш баланс: {balance}"
    await message.answer(text)


@dp.message_handler(Text("Мои рефералы"))
async def check_user_referral(message: Message):
    referrals = await database.get_referrals()
    if referrals:
        text = f"Ваши рефералы:\n{referrals}"
    else:
        text = "У вас нет ни одного реферала"
    await message.answer(text)


@dp.message_handler(Text("Добавить монет"))
async def add_random_money(message: Message):
    random_amount = random.randint(1, 100)
    await database.add_money(random_amount)
    balance = await database.check_balance()
    text = f"""
Вам было добавлено {random_amount} монет.
Теперь ваш баланс: {balance}
        """
    await message.answer(text)


@dp.message_handler(Text("Реферальнная сылка"))
async def show_referral_link(message: Message):
    user_id = await database.get_id()

    bot_username = (await bot.me).username
    bot_link = f"https://t.me/{bot_username}?start={user_id}"

    text = f"Ваша реферальная ссылка: {bot_link}"

    await message.answer(text)


@dp.message_handler(Text("Скрыть меню"))
async def hide_menu(message: Message):
    await message.answer(text="Пока", reply_markup=ReplyKeyboardRemove())
