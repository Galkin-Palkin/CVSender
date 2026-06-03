import os
from posixpath import basename
from aiogram.types import Message
from aiogram import Bot

from constants import STORAGE_DIR


async def download_document(message: Message, bot: Bot):
    download_destination = os.path.join(STORAGE_DIR, basename(message.document.file_name))
    await bot.download(message.document, download_destination)
