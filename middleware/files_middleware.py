from aiogram import BaseMiddleware

from strings import UNSUPPORTED_FILE_EXTENSION

class FileMiddleware(BaseMiddleware):
    def __init__(self, allowed_mime_types: list[str]):
        super().__init__()
        self.allowed_mime_types = allowed_mime_types

    async def __call__(self, handler, event, data):
        if event.document is None:
            return await handler(event, data)

        if not (event.document.mime_type in self.allowed_mime_types):
            await event.reply(text=UNSUPPORTED_FILE_EXTENSION)
            return None

        return await handler(event, data)
