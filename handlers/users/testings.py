from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from loader import dp
from states.test import Test


@dp.message_handler(Command("test"))
async def test_begin(message: Message):
    await message.answer("Вы начали тест.\n"
                         "Вопрос 1:\n"
                         "Ваше имя?")

    await Test.first()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data["name"] = answer

    await message.answer("Вопрос 2:\n"
                         "Ваш возраст?")

    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q1(message: Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data["old"] = answer

    await message.answer("Вопрос 3:\n"
                         "Ваша мечта?")

    await Test.next()


@dp.message_handler(state=Test.Q3)
async def answer_q1(message: Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data["dream"] = answer

    await message.answer("Спасибо за прохождение опроса.")

    await state.finish()


