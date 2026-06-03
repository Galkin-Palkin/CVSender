import logging

from aiogram import Bot
from dotenv import load_dotenv
from constants import ALLOWED_MIME_TYPES
from middleware.files_middleware import FileMiddleware
from middleware.bot_middleware import BotMiddleware
from handlers import cv_files, cv_letters, cv_titles, email_credentials
from handlers.main import dp
import asyncio
import os

from middleware.user_middleware import UserMiddleware

async def main():
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    bot = Bot(token=os.getenv("TG_BOT_TOKEN"))
    dp.include_routers(cv_files.router, cv_letters.router, cv_titles.router, email_credentials.router)
    dp.update.outer_middleware(UserMiddleware()) # Чтобы только сам человек имел доступ к резюме
    dp.update.middleware(BotMiddleware(bot=bot))
    dp.message.outer_middleware(FileMiddleware(allowed_mime_types=ALLOWED_MIME_TYPES))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
