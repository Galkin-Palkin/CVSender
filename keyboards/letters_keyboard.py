from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callback_data import CallbackData
from entity.letter import Letter
from strings import DELETE_LETTER_PATTERN_BUTTON, EDIT_LETTER_NAME_BUTTON, EDIT_LETTER_PATTERN_BUTTON, CREATE_NEW_LETTER_BUTTON

def letters_menu_keyboard(letters: list[Letter]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    create_new_letter_button = InlineKeyboardButton(text=CREATE_NEW_LETTER_BUTTON, callback_data=CallbackData.create_new_letter)
    builder.add(create_new_letter_button)
    for letter in letters:
        button = InlineKeyboardButton(text=letter.name, callback_data=CallbackData.letter(letter.id))
        builder.add(button)
    builder.adjust(1)
    return builder.as_markup()

def letter_menu_keyboard(letter: Letter) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=EDIT_LETTER_NAME_BUTTON, callback_data=CallbackData.edit_letter_name(letter.id))],
            [InlineKeyboardButton(text=EDIT_LETTER_PATTERN_BUTTON, callback_data=CallbackData.edit_letter_pattern(letter.id))],
            [InlineKeyboardButton(text=DELETE_LETTER_PATTERN_BUTTON, callback_data=CallbackData.delete_letter_pattern(letter.id))]
        ]
    )
