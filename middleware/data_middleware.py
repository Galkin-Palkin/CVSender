from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject

from repository.file_repository import CVFileRepository
from repository.letter_repository import LetterRepository
from repository.title_repository import TitleRepository

class DataMiddleware(BaseMiddleware):
    def __init__(self, title_repository: TitleRepository, letter_repository: LetterRepository, cv_file_repository: CVFileRepository):
        self.title_repository = title_repository
        self.letter_repository = letter_repository 
        self.cv_file_repository = cv_file_repository
        pass

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ):
        data['title_repository'] = self.title_repository
        data['letter_repository'] = self.letter_repository
        data['cv_file_repository'] = self.cv_file_repository
        return await handler(event, data)
