import logging
import os

import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text as TextFilter
from aiogram.dispatcher.filters.state import State, StatesGroup

import keyboard as kb
import pension

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=["start"])
async def send_welcome(message):
    await message.answer(
        "ПРИВЕТСТВИЕ",
        reply_markup=kb.agree_markup,
    )


@dp.message_handler(TextFilter(equals=kb.UNDERSTAND_BUTTON))
async def send_main_keyboard(message):
    await message.answer(
        "Воспользуйтесь клавиатурой",
        reply_markup=kb.main_markup,
    )


@dp.message_handler(TextFilter(equals=kb.PENSION_BUTTON))
async def send_pension_willingness(message):
    from pension import PENSION_PERIOD

    await message.answer(
        PENSION_PERIOD,
        reply_markup=kb.pension_period_markup,
    )


@dp.message_handler(TextFilter(equals=kb.MONTH_PERIOD_BUTTON))
async def send_month_period(message):
    await message.answer(
        "Текст если остался месяц до пенсии",
        reply_markup=kb.pension_documents_markup,
    )


@dp.message_handler(TextFilter(equals=kb.YEAR_PERIOD_BUTTON))
async def send_year_period(message):
    from pension import PENSION_YEAR_PERIOD

    await message.answer(
        PENSION_YEAR_PERIOD,
        reply_markup=kb.need_documents_markup,
    )


@dp.message_handler(TextFilter(equals=kb.NEED_DOCUMENTS_BUTTON))
async def send_need_documents(message):
    from pension import NEED_DOCUMENTS

    await message.answer(
        NEED_DOCUMENTS,
        reply_markup=kb.need_documents_markup,
    )


@dp.message_handler(TextFilter(equals=kb.SCHEDULE_BUTTON))
async def send_schedule(message):
    from pension import SCHEDULE

    await message.answer(
        SCHEDULE,
        reply_markup=kb.need_documents_markup,
    )


@dp.message_handler(TextFilter(equals=kb.BACK_BUTTON))
async def send_back(message):
    await message.answer(
        "Воспользуйтесь клавиатурой",
        reply_markup=kb.main_markup,
    )


@dp.message_handler(TextFilter(equals=kb.DOCUMENTS_MADE), state="*")
async def send_statement(message):
    await message.answer(
        "Через что идет подача заявления",
        reply_markup=kb.statement_pension_markup,
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
