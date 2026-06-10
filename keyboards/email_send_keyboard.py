from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from callback_data import CallbackData
from strings import EDIT_EMAILS_TO_SEND_BUTTON, EDIT_FILES_BUTTON, EDIT_LETTER_BUTTON, EDIT_TITLE_BUTTON, SEND_CV_BUTTON


def email_send_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=EDIT_FILES_BUTTON, callback_data=CallbackData.edit_files)],
            [InlineKeyboardButton(text=EDIT_TITLE_BUTTON, callback_data=CallbackData.edit_title)],
            [InlineKeyboardButton(text=EDIT_LETTER_BUTTON, callback_data=CallbackData.edit_letter)],
            [InlineKeyboardButton(text=EDIT_EMAILS_TO_SEND_BUTTON, callback_data=CallbackData.edit_emails_to_send)],
            [InlineKeyboardButton(text=SEND_CV_BUTTON, callback_data=CallbackData.send_cv)],
        ]
    )