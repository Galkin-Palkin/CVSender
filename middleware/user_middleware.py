from asyncio.log import logger

from aiogram import BaseMiddleware
from aiogram.types import User

from constants import ALLOWED_USER_ID

class UserMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        user: User | None = data.get("event_from_user")

        if user != None and user.id.__str__() != ALLOWED_USER_ID:
            logger.warning(msg=f"Attempt of unauthorized access: user_id = {user.id}")
            return None

        return await handler(event, data)
