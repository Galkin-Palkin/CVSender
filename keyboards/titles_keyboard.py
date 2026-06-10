from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callback_data import CallbackData
from entity.title import Title
from strings import DELETE_TITLE_PATTERN_BUTTON, EDIT_TITLE_PATTERN_BUTTON

def titles_keyboard(titles: list[Title]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=title.title, callback_data=CallbackData.title(title.id))] for title in titles
        ]
    )

def title_menu_keyboard(title: Title) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=EDIT_TITLE_PATTERN_BUTTON, callback_data=CallbackData.edit_title_pattern(title.id))],
            [InlineKeyboardButton(text=DELETE_TITLE_PATTERN_BUTTON, callback_data=CallbackData.delete_title_pattern(title.id))]
        ]
    )
