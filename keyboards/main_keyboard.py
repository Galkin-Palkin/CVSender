from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from callback_data import CallbackData
from strings import LETTER_PATTERNS_BUTTON, TITLE_PATTERNS_BUTTON, EMAIL_CREDENTIALS_BUTTON, SEND_CV_BUTTON 

def main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=LETTER_PATTERNS_BUTTON, callback_data=CallbackData.cv_letters)],
        [InlineKeyboardButton(text=TITLE_PATTERNS_BUTTON, callback_data=CallbackData.cv_titles)],
        [InlineKeyboardButton(text=EMAIL_CREDENTIALS_BUTTON, callback_data=CallbackData.email_credentials)],
        [InlineKeyboardButton(text=SEND_CV_BUTTON, callback_data=CallbackData.email_send)],
    ])
