from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.main_keyboard import main_keyboard
from strings import MAIN_MENU

dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.reply(text=MAIN_MENU, reply_markup=main_keyboard())
