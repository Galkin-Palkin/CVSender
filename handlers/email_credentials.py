from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

from callback_data import CallbackData
from keyboards.email_keyboard import edit_credentials_keyboard, email_keyboard
from states import GmailComEdit, GmailComPasswordEdit, MailRuEdit, MailRuPasswordEdit
from strings import EDIT_GMAIL_COM_MESSAGE, EDIT_GMAIL_COM_PASSWORD_MESSAGE, EDIT_MAIL_RU_MESSAGE, EDIT_MAIL_RU_PASSWORD_MESSAGE, EMAIL_MENU, GMAIL_COM_MENU, MAIL_RU_MENU, SUCCESSFUL_GMAIL_COM_EDIT, SUCCESSFUL_GMAIL_COM_PASSWORD_EDIT, SUCCESSFUL_MAIL_RU_EDIT, SUCCESSFUL_MAIL_RU_PASSWORD_EDIT
from aiogram.fsm.context import FSMContext

router = Router()

@router.callback_query(F.data == CallbackData.email_credentials)
async def email_credentials_menu(callback: CallbackQuery):
    await callback.message.answer(text=EMAIL_MENU, reply_markup=email_keyboard())
    await callback.answer()


#  Mail.ru

@router.callback_query(F.data == CallbackData.mail_ru)
async def mail_ru(callback: CallbackQuery):
    await callback.message.answer(text=MAIL_RU_MENU, reply_markup=edit_credentials_keyboard(email=CallbackData.mail_ru))
    await callback.answer()

@router.callback_query(F.data == CallbackData.edit_email(CallbackData.mail_ru))
async def edit_mail_ru(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=EDIT_MAIL_RU_MESSAGE)
    await callback.answer()
    await state.set_state(MailRuEdit.state)

@router.callback_query(F.data == CallbackData.edit_password(CallbackData.mail_ru))
async def edit_mail_ru_password(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=EDIT_MAIL_RU_PASSWORD_MESSAGE)
    await callback.answer()
    await state.set_state(MailRuPasswordEdit.state)

@router.message(MailRuEdit.state)
async def mail_ru_email_input(message: Message):
    new_email = message.text
    await message.answer(text=SUCCESSFUL_MAIL_RU_EDIT)

@router.message(MailRuPasswordEdit.state)
async def mail_ru_password_input(message: Message):
    new_password = message.text
    await message.answer(text=SUCCESSFUL_MAIL_RU_PASSWORD_EDIT)

#  Gmail.com

@router.callback_query(F.data == CallbackData.gmail_com)
async def gmail_com(callback: CallbackQuery):
    await callback.message.answer(text=GMAIL_COM_MENU, reply_markup=edit_credentials_keyboard(email=CallbackData.gmail_com))
    await callback.answer()


@router.callback_query(F.data == CallbackData.edit_email(CallbackData.gmail_com))
async def edit_gmail_com(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=EDIT_GMAIL_COM_MESSAGE)
    await callback.answer()
    await state.set_state(GmailComEdit.state)
    

@router.callback_query(F.data == CallbackData.edit_password(CallbackData.gmail_com))
async def edit_gmail_com_password(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=EDIT_GMAIL_COM_PASSWORD_MESSAGE)
    await callback.answer()
    await state.set_state(GmailComPasswordEdit.state)

@router.message(GmailComEdit.state)
async def gmail_com_email_input(message: Message):
    new_email = message.text
    await message.answer(text=SUCCESSFUL_GMAIL_COM_EDIT)

@router.message(GmailComPasswordEdit.state)
async def gmail_com_password_input(message: Message):
    new_password = message.text
    await message.answer(text=SUCCESSFUL_GMAIL_COM_PASSWORD_EDIT)

#TODO подумать над обобщением методов - их как-то очень много и они подозрительно похожи
# Стоит также подумать над проверкой того, что ввод от пользователя действительно является почтой или паролем, а не чем-то случайным.
# Если добавлю reply кнопки - надо добавить мидлварь, который будет проверять, что при ожидании ввода от пользователя не был прислан текст ReplyButton