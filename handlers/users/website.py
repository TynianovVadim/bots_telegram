from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline import choice
from keyboards.inline.callback_datas import open_website_callback
from keyboards.inline.website_buttons import youtube_button, google_button, github_button

from loader import dp


@dp.message_handler(Command("site"))
async def make_choice(message: Message):
    await message.answer(text="Choice website", reply_markup=choice)


@dp.callback_query_handler(open_website_callback.filter(site_name="youtube"))
async def open_yt(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(f"{callback_data['site_name']}", reply_markup=youtube_button)


@dp.callback_query_handler(open_website_callback.filter(site_name="google"))
async def open_yt(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(f"{callback_data['site_name']}", reply_markup=google_button)


@dp.callback_query_handler(open_website_callback.filter(site_name="github"))
async def open_yt(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(f"{callback_data['site_name']}", reply_markup=github_button)


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.delete()
