from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from callback_data import CallbackData
from keyboards.letters_keyboard import letter_menu_keyboard, letters_menu_keyboard
from strings import CERTAIN_LETTER_MENU, LETTERS_MENU

router = Router()

@router.callback_query(F.data == CallbackData.cv_letters)
async def letters_menu(callback: CallbackQuery):
    await callback.message.answer(text=LETTERS_MENU, reply_markup=letters_menu_keyboard())
    await callback.answer()

@router.callback_query(F.data.startswith(CallbackData.letter_prefix))
async def certain_letter_menu(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=CERTAIN_LETTER_MENU(""), reply_markup=letter_menu_keyboard())
    await callback.answer()

# Присылать моноширинный текст письма, чтобы его можно было скопировать и вставить
@router.callback_query(F.data.startswith(CallbackData.edit_letter_prefix))
async def edit_letter(callback: CallbackQuery, state: FSMContext):
    pass

@router.callback_query(F.data.startswith(CallbackData.delete_letter_prefix))
async def delete_letter(callback: CallbackQuery, state: FSMContext):
    pass

@router.callback_query(F.data == "")
async def back_to_main_menu():
    pass