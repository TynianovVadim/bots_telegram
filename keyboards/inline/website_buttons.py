from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import URL_YOUTUBE, URL_GOOGLE, URL_GIT

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Open YouTube", callback_data="open:youtube"),
            InlineKeyboardButton(text="Open Google", callback_data="open:google"),
            InlineKeyboardButton(text="Open GitHub", callback_data="open:github"),
        ],
        [
            InlineKeyboardButton(text="Cancel", callback_data="cancel"),
        ]
    ]
)

youtube_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Open", url=URL_YOUTUBE)]
    ]
)

google_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Open", url=URL_GOOGLE)]
    ]
)

github_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Open", url=URL_GIT)]
    ]
)
