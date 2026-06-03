from posixpath import basename

from aiogram import Bot, Router
from aiogram import F
from aiogram.types import Message
from strings import DOCUMENT_DOWNLOADED_SUCCESSFULLY
from utils.download import download_document

router = Router()
    
@router.message(F.document)
async def receive_cv_files(message: Message, bot: Bot):
    await download_document(message, bot)
    document_name = basename(message.document.file_name)
    await bot.send_message(chat_id=message.chat.id, text=DOCUMENT_DOWNLOADED_SUCCESSFULLY(document_name))
