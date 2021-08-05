import logging
import os

import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=["start"], state="*")
async def send_welcome(message):
    await message.answer(
        "Памятка"
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)