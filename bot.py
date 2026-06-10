import logging

from aiogram import Bot
from dotenv import load_dotenv
from constants import ALLOWED_MIME_TYPES
from middleware.files_middleware import FileMiddleware
from middleware.bot_middleware import BotMiddleware
from handlers import cv_files, cv_letters, cv_titles, email_send
from handlers.main import dp
import asyncio
import os

from middleware.user_middleware import UserMiddleware

#TODO добавить обработку ошибок, например, при вводе некорректного шаблона письма или резюме, для почты
#TODO добавить ИИ (от разных компаний - Гигачат, OpenAI и тд) - для генерации шаблонов писем и их редактирования
#TODO добавить в README инструкцию по установке бота и зависимостей, а также по его использованию
#TODO убрать email_credentials совсем: почту и пароль можно хранить в .env
#TODO сделать проверку, что пользователь ввёл корректные учетные данные для почты, например, отправив тестовое письмо на свой адрес

async def main():
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    bot = Bot(token=os.getenv("TG_BOT_TOKEN"))
    dp.include_routers(cv_files.router, cv_letters.router, cv_titles.router, email_send.router)
    dp.update.outer_middleware(UserMiddleware()) # Чтобы только сам человек имел доступ к резюме
    dp.update.middleware(BotMiddleware(bot=bot))
    dp.message.outer_middleware(FileMiddleware(allowed_mime_types=ALLOWED_MIME_TYPES))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
