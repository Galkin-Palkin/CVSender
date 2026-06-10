from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callback_data import CallbackData
from entity.letter import Letter
from strings import DELETE_LETTER_PATTERN_BUTTON, EDIT_LETTER_PATTERN_BUTTON

def letters_menu_keyboard(letters: list[Letter]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=letter.name, callback_data=CallbackData.letter(letter.id))] for letter in letters
        ]
    )

def letter_menu_keyboard(letter: Letter) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=EDIT_LETTER_PATTERN_BUTTON, callback_data=CallbackData.edit_letter_pattern(letter.id))],
            [InlineKeyboardButton(text=DELETE_LETTER_PATTERN_BUTTON, callback_data=CallbackData.delete_letter_pattern(letter.id))]
        ]
    )
