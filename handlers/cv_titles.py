from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from callback_data import CallbackData
from keyboards.letters_keyboard import letter_menu_keyboard, letters_menu_keyboard
from strings import CERTAIN_TITLE_MENU, TITLES_MENU

router = Router()

@router.callback_query(F.data == CallbackData.cv_titles)
async def titles_menu(callback: CallbackQuery):
    await callback.message.answer(text=TITLES_MENU, reply_markup=letters_menu_keyboard())
    await callback.answer()

@router.callback_query(F.data.startswith(CallbackData.title_prefix))
async def certain_title_menu(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=CERTAIN_TITLE_MENU(""), reply_markup=letter_menu_keyboard())
    await callback.answer()

# Присылать моноширинный текст письма, чтобы его можно было скопировать и вставить
@router.callback_query(F.data.startswith(CallbackData.edit_title_prefix))
async def edit_title(callback: CallbackQuery, state: FSMContext):
    pass

@router.callback_query(F.data.startswith(CallbackData.delete_title_prefix))
async def delete_title(callback: CallbackQuery, state: FSMContext):
    pass

@router.callback_query(F.data == "")
async def back_to_main_menu():
    pass