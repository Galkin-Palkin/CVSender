from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from callback_data import CallbackData
from constants import LETTER_ID
from database import dummy_data
from keyboards.letters_keyboard import letter_menu_keyboard, letters_menu_keyboard
from states import LetterEdit
from strings import CERTAIN_LETTER_MENU, EDIT_LETTER_MESSAGE, LETTER_DELETED_SUCCESSFULLY, LETTERS_MENU, SUCCESSFUL_LETTER_EDIT_MESSAGE
from utils.id_helper import IdHelper

router = Router()

@router.callback_query(F.data == CallbackData.cv_letters)
async def letters_menu(callback: CallbackQuery):
    await callback.message.answer(text=LETTERS_MENU, reply_markup=letters_menu_keyboard(letters=dummy_data.letters))
    await callback.answer()

@router.callback_query(F.data.startswith(CallbackData.letter_prefix))
async def certain_letter_menu(callback: CallbackQuery, state: FSMContext):
    letter_id = await IdHelper.add_id_to_state(callback.data, state, LETTER_ID)
    await callback.message.answer(text=CERTAIN_LETTER_MENU(str(letter_id)), reply_markup=letter_menu_keyboard())
    await callback.answer()

# Присылать моноширинный текст письма, чтобы его можно было скопировать и вставить
@router.callback_query(F.data.startswith(CallbackData.edit_letter_prefix))
async def edit_letter(callback: CallbackQuery, state: FSMContext):
    letter_id = await IdHelper.add_id_to_state(callback.data, state, LETTER_ID)
    await callback.message.answer(text=EDIT_LETTER_MESSAGE)
    await callback.answer()
    await state.set_state(LetterEdit.state)

@router.callback_query(F.data.startswith(CallbackData.delete_letter_prefix))
async def delete_letter(callback: CallbackQuery, state: FSMContext):
    letter_id = await IdHelper.add_id_to_state(callback.data, state, LETTER_ID)
    await callback.message.answer(text=LETTER_DELETED_SUCCESSFULLY)
    await callback.answer()

@router.message(LetterEdit.state & ~F.command)
async def letter_input(message: Message, state: FSMContext):
    letter_id = await IdHelper.get_id_from_state(state, LETTER_ID)
    new_title = message.text
    await message.answer(text=SUCCESSFUL_LETTER_EDIT_MESSAGE)
    await state.clear_state()

@router.callback_query(F.data == "")
async def back_to_main_menu():
    pass