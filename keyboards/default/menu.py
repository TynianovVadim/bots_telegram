from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("Мой баланс"),
            KeyboardButton("Добавить монет")
         ],
        [
            KeyboardButton("Мои рефералы"),
            KeyboardButton("Реферальнная сылка")
        ],
        [
            KeyboardButton("Скрыть меню")
        ]

    ],
    resize_keyboard=True
)
