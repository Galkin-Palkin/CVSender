from aiogram import F, Router
from aiogram.types import CallbackQuery

from callback_data import CallbackData
from keyboards.files_keyboard import files_keyboard
from keyboards.email_send_keyboard import email_send_keyboard
from database.dummy_data import files
from strings import EDIT_FILES_MENU, EMAIL_SEND_MENU
from utils.id_helper import IdHelper


router = Router()

@router.callback_query(F.data == CallbackData.email_send)
async def email_send(callback: CallbackQuery):
    await callback.message.answer(text=EMAIL_SEND_MENU, reply_markup=email_send_keyboard())
    await callback.answer()
    

@router.callback_query(F.data == CallbackData.edit_files)
async def edit_files(callback: CallbackQuery):
    await callback.message.answer(text=EDIT_FILES_MENU, reply_markup=files_keyboard(files))
    await callback.answer()
    
@router.callback_query(F.data.startswith(CallbackData.file_selected_prefix))
async def file_selected(callback: CallbackQuery):
    file_id = IdHelper.extract_id(callback_data=callback.data)
    #TODO добавить обработку нажатия на кнопку
    await callback.answer()
    
@router.callback_query(F.data.startswith(CallbackData.file_unselected_prefix))
async def file_unselected(callback: CallbackQuery):
    file_id = IdHelper.extract_id(callback_data=callback.data)
    #TODO добавить обработку нажатия на кнопку
    await callback.answer()
    