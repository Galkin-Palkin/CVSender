from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from callback_data import CallbackData
from constants import LETTER_ID, TITLE_ID
from database import dummy_data
from keyboards.letters_keyboard import letter_menu_keyboard, letters_menu_keyboard
from keyboards.titles_keyboard import title_menu_keyboard
from states import TitleEdit
from strings import CERTAIN_TITLE_MENU, EDIT_TITLE_PATTERN_MESSAGE, SUCCESSFUL_TITLE_PATTERN_EDIT_MESSAGE, TITLE_PATTERN_DELETED_SUCCESSFULLY, TITLES_MENU
from utils.id_helper import IdHelper

router = Router()

@router.callback_query(F.data == CallbackData.cv_titles)
async def titles_menu(callback: CallbackQuery):
    await callback.message.answer(text=TITLES_MENU, reply_markup=title_menu_keyboard(titles=dummy_data.titles))
    await callback.answer()

@router.callback_query(F.data.startswith(CallbackData.title_prefix))
async def certain_title_menu(callback: CallbackQuery, state: FSMContext):
    title_id = await IdHelper.add_id_to_state(callback.data, state, TITLE_ID)
    await callback.message.answer(text=CERTAIN_TITLE_MENU(), reply_markup=letter_menu_keyboard())
    await callback.answer()
    
# Присылать моноширинный текст письма, чтобы его можно было скопировать и вставить
@router.callback_query(F.data.startswith(CallbackData.edit_title_prefix))
async def edit_title(callback: CallbackQuery, state: FSMContext):
    title_id = await IdHelper.add_id_to_state(callback.data, state, TITLE_ID)
    await callback.message.answer(text=EDIT_TITLE_PATTERN_MESSAGE)
    await callback.answer()
    await state.set_state(TitleEdit.state)

@router.callback_query(F.data.startswith(CallbackData.delete_title_prefix))
async def delete_title(callback: CallbackQuery, state: FSMContext):
    title_id = await IdHelper.add_id_to_state(callback.data, state, TITLE_ID)
    await callback.message.answer(text=TITLE_PATTERN_DELETED_SUCCESSFULLY)
    await callback.answer()

@router.message(TitleEdit.state & ~F.command)
async def title_input(message: Message, state: FSMContext):
    data = await state.get_data()
    title_id = data.get(TITLE_ID)
    new_title = message.text
    await message.answer(text=SUCCESSFUL_TITLE_PATTERN_EDIT_MESSAGE)
    await state.clear_state()

@router.callback_query(F.data == "")
async def back_to_main_menu():
    pass