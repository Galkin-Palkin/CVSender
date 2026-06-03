from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject

class BotMiddleware(BaseMiddleware):
    def __init__(self, bot: Bot):
        self.bot = bot
        pass

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ):
        data['bot'] = self.bot
        return await handler(event, data)
