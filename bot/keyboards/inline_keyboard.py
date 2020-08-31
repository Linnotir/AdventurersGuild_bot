from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Example Keyboard
example_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='v1.0', callback_data='v10'),
        InlineKeyboardButton(text='v1.1', callback_data='v11'),
        InlineKeyboardButton(text='v1.2', callback_data='v12'),
        InlineKeyboardButton(text='v1.3', callback_data='v13'),
        InlineKeyboardButton(text='v1.3.3', callback_data='v133'),
    ],
    [
        InlineKeyboardButton(text='Закрыть', callback_data='cancel')
    ]
])