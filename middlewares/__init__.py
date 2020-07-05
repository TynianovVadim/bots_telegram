from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware
from .language_middleware import setup_middleware


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
