import logging

from aiogram import Bot
from dotenv import load_dotenv
from constants import ALLOWED_MIME_TYPES
from database.database import DatabaseV1
from middleware.data_middleware import DataMiddleware
from middleware.files_middleware import FileMiddleware
from middleware.bot_middleware import BotMiddleware
from handlers import cv_files, cv_letters, cv_titles, email_send
from handlers.main import dp
import asyncio
import os

from middleware.user_middleware import UserMiddleware
from repository.file_repository import CVFileRepository
from repository.letter_repository import LetterRepository
from repository.title_repository import TitleRepository

#TODO добавить обработку ошибок, например, при вводе некорректного шаблона письма или резюме, для почты
#TODO добавить ИИ (от разных компаний - Гигачат, OpenAI и тд) - для генерации шаблонов писем и их редактирования
#TODO добавить в README инструкцию по установке бота и зависимостей, а также по его использованию
#TODO сделать проверку, что пользователь ввёл корректные учетные данные для почты, например, отправив тестовое письмо на свой адрес

def init_db_and_repositories():
    database = DatabaseV1()
    title_repository = TitleRepository(connection=database.connection)
    letter_repository = LetterRepository(connection=database.connection) 
    cv_file_repository = CVFileRepository(connection=database.connection)
    return (database, title_repository, letter_repository, cv_file_repository)

async def main():
    database, title_repository, letter_repository, cv_file_repository = init_db_and_repositories()
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    database.create_database_if_not_exist()
    bot = Bot(token=os.getenv("TG_BOT_TOKEN"))
    dp.include_routers(cv_files.router, cv_letters.router, cv_titles.router, email_send.router)
    dp.update.outer_middleware(UserMiddleware()) # Чтобы только сам человек имел доступ к резюме
    dp.update.middleware(BotMiddleware(bot=bot))
    dp.update.middleware(
        DataMiddleware(
            title_repository=title_repository,
            letter_repository=letter_repository,
            cv_file_repository=cv_file_repository
        )
    )
    dp.message.outer_middleware(FileMiddleware(allowed_mime_types=ALLOWED_MIME_TYPES))
    try:
        await dp.start_polling(bot)
    finally:
        database.close()

if __name__ == "__main__":
    asyncio.run(main())
