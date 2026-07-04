import uuid

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from callback_data import CallbackData
from constants import HTML_PARSE_MODE, LETTER_ID, LETTER_NAME, LETTER_TEXT
from database import dummy_data
from entity.letter import Letter
from keyboards.letters_keyboard import letter_menu_keyboard, letters_menu_keyboard
from repository.letter_repository import LetterRepository
from states import CreateNewLetter, LetterEdit, LetterNameEdit
from strings import CERTAIN_LETTER_MENU, EDIT_LETTER_NAME_MESSAGE, EDIT_LETTER_PATTERN_MESSAGE, LETTER_CREATED_SUCCESSFULLY, LETTER_NAME_MESSAGE, LETTER_PATTERN_DELETED_SUCCESSFULLY, LETTER_TEXT_MESSAGE, LETTERS_MENU, SUCCESSFUL_LETTER_PATTERN_EDIT_MESSAGE
from utils.id_helper import StateHelper
from utils.uuid import get_new_uuid

router = Router()

#TODO добавить ввод названия шаблона письма

@router.callback_query(F.data == CallbackData.cv_letters)
async def letters_menu(callback: CallbackQuery, letter_repository: LetterRepository):
    letters = letter_repository.get_all_letters()
    await callback.message.answer(text=LETTERS_MENU, reply_markup=letters_menu_keyboard(letters=letters))
    await callback.answer()

@router.callback_query(F.data == CallbackData.create_new_letter)
async def create_new_letter(callback: CallbackQuery, state: FSMContext):
    letter_id = get_new_uuid()
    await StateHelper.add_value_to_state(state=state, key=LETTER_ID, value=letter_id)
    await callback.message.answer(text=LETTER_NAME_MESSAGE)
    await callback.answer()
    await state.set_state(CreateNewLetter.name_input)

@router.message(CreateNewLetter.name_input, ~F.text.startswith("/"))
async def letter_name_input(message: Message, state: FSMContext):
    letter_name = message.text
    #TODO Добавить фильтр-проверку на правильность ввода
    await StateHelper.add_value_to_state(state=state, key=LETTER_NAME, value=letter_name)
    await message.answer(text=LETTER_TEXT_MESSAGE)
    await state.set_state(CreateNewLetter.letter_text_input)

@router.message(CreateNewLetter.letter_text_input, ~F.text.startswith("/"))
async def letter_text_input(message: Message, state: FSMContext, letter_repository: LetterRepository):
    letter_id = await StateHelper.get_value_from_state(state=state, key=LETTER_ID)
    letter_name = await StateHelper.get_value_from_state(state=state, key=LETTER_NAME)
    letter_text = message.text
    letter = Letter(
        id=letter_id,
        name=letter_name,
        text=letter_text
    )
    #TODO Добавить фильтр-проверку на правильность ввода
    letter_repository.add_letter(letter=letter)
    await message.answer(text=LETTER_CREATED_SUCCESSFULLY)
    await state.clear()

@router.callback_query(F.data.startswith(CallbackData.letter_prefix))
async def certain_letter_menu(callback: CallbackQuery, state: FSMContext, letter_repository: LetterRepository):
    letter_id = await StateHelper.add_id_to_state(callback.data, state, LETTER_ID)
    letter = letter_repository.get_letter(letter_id=letter_id)
    await callback.message.answer(text=CERTAIN_LETTER_MENU(letter.text), reply_markup=letter_menu_keyboard(letter=letter), parse_mode=HTML_PARSE_MODE)
    await callback.answer()

# Присылать моноширинный текст письма, чтобы его можно было скопировать и вставить
@router.callback_query(F.data.startswith(CallbackData.edit_letter_name_prefix))
async def edit_letter_name(callback: CallbackQuery, state: FSMContext):
    _ = await StateHelper.add_id_to_state(callback.data, state, LETTER_ID)
    await callback.message.answer(text=EDIT_LETTER_NAME_MESSAGE)
    await callback.answer()
    await state.set_state(LetterNameEdit.state)

# Присылать моноширинный текст письма, чтобы его можно было скопировать и вставить
@router.callback_query(F.data.startswith(CallbackData.edit_letter_prefix))
async def edit_letter(callback: CallbackQuery, state: FSMContext):
    _ = await StateHelper.add_id_to_state(callback.data, state, LETTER_ID)
    await callback.message.answer(text=EDIT_LETTER_PATTERN_MESSAGE)
    await callback.answer()
    await state.set_state(LetterEdit.state)

@router.callback_query(F.data.startswith(CallbackData.delete_letter_prefix))
async def delete_letter(callback: CallbackQuery, state: FSMContext, letter_repository: LetterRepository):
    letter_id = await StateHelper.add_id_to_state(callback.data, state, LETTER_ID)
    letter_repository.delete_letter(letter_id=letter_id)
    await callback.message.answer(text=LETTER_PATTERN_DELETED_SUCCESSFULLY)
    await callback.answer()

@router.message(LetterEdit.state, ~F.text.startswith("/"))
async def letter_input(message: Message, state: FSMContext, letter_repository: LetterRepository):
    letter_id = await StateHelper.get_value_from_state(state, LETTER_ID)
    old_letter = letter_repository.get_letter(letter_id=letter_id)
    new_text = message.text
    letter_name = old_letter.name
    new_letter = Letter(
        id=letter_id,
        name=letter_name,
        text=new_text
    )
    letter_repository.update_letter(new_letter)
    await message.answer(text=SUCCESSFUL_LETTER_PATTERN_EDIT_MESSAGE)
    await state.clear()


@router.message(LetterNameEdit.state, ~F.text.startswith("/"))
async def letter_name_input(message: Message, state: FSMContext, letter_repository: LetterRepository):
    letter_id = await StateHelper.get_value_from_state(state, LETTER_ID)
    old_letter = letter_repository.get_letter(letter_id=letter_id)
    new_name = message.text
    letter_text = old_letter.text
    new_letter = Letter(
        id=letter_id,
        name=new_name,
        text=letter_text
    )
    letter_repository.update_letter(new_letter)
    await message.answer(text=SUCCESSFUL_LETTER_PATTERN_EDIT_MESSAGE)
    await state.clear()

@router.callback_query(F.data == "")
async def back_to_main_menu():
    pass