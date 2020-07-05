from typing import Tuple, Any

from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram import types
from data.config import I18N_DOMAIN, LOCALES_DIR

from utils.db_api.database import DBCommands


db = DBCommands()


async def get_language(user_id):
    # запрос к базе данных
    user = await db.get_user(user_id)
    if user:
        return user.language


class ACLMiddleware(I18nMiddleware):
    # узнаем язык полбзователя
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        user = types.User.get_current()
        return await get_language(user.id) or user.locale


def setup_middleware(dp):
    # установка мидлвферов
    i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
    dp.middleware.setup(i18n)
    return i18n
