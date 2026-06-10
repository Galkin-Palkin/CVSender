from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callback_data import CallbackData
from entity.cv_file import CVFile
from strings import FILE_NOT_SELECTED, FILE_SELECTED

def _file_title(file: CVFile) -> str:
    if file.selected:
        return FILE_SELECTED(file.name)
    
    return FILE_NOT_SELECTED(file.name)

def _file_callback_data(file: CVFile) -> str:
    # Инвертируем: когда файл выбран, нажатие на кнопку должно отменять то, что файл выбран
    if file.selected:
        return CallbackData.file_unselected(file.id)
    
    return CallbackData.file_selected(file.id)

def _init_button(file: CVFile) -> InlineKeyboardButton:
    return InlineKeyboardButton(
        text = _file_title(file=file),
        callback_data=_file_callback_data(file=file)
    )

def files_keyboard(files: list[CVFile]):
    builder = InlineKeyboardBuilder()
    for file in files:
         builder.add(_init_button(file))
    builder.adjust(1)
    return builder.as_markup()
    
#TODO добавить в email_send_keyboard.py handlers для file_selected & file_unselected