from aiogram.fsm.state import State, StatesGroup

class GmailComEdit(StatesGroup):
    state = State()

class GmailComPasswordEdit(StatesGroup):
    state = State()

class MailRuEdit(StatesGroup):
    state = State()

class MailRuPasswordEdit(StatesGroup):
    state = State()

class LetterEdit(StatesGroup):
    state = State()

class TitleEdit(StatesGroup):
    state = State()
