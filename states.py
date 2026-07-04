from aiogram.fsm.state import State, StatesGroup

class LetterEdit(StatesGroup):
    state = State()

class TitleEdit(StatesGroup):
    state = State()

class CreateNewLetter(StatesGroup):
    name_input = State()
    letter_text_input = State()

class LetterNameEdit(StatesGroup):
    state = State()
    