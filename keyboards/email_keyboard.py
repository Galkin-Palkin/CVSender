from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from callback_data import CallbackData
from strings import EDIT_EMAIL_BUTTON, EDIT_PASSWORD_BUTTON, GMAIL_COM_BUTTON, MAIL_RU_BUTTON

def email_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=MAIL_RU_BUTTON, callback_data=CallbackData.mail_ru)],
            [InlineKeyboardButton(text=GMAIL_COM_BUTTON, callback_data=CallbackData.gmail_com)]
        ]
    )

# Указать как параметр CallbackData.mail_ru или CallbackData.gmail_com, в зависимости от места вызова
def edit_credentials_keyboard(email: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=EDIT_EMAIL_BUTTON, callback_data=CallbackData.edit_email(email))],
            [InlineKeyboardButton(text=EDIT_PASSWORD_BUTTON, callback_data=CallbackData.edit_password(email))]
        ]
    )
