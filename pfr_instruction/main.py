import logging
import os

import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text as TextFilter
from aiogram.dispatcher.filters.state import State, StatesGroup

from . import keyboard as kb
from . import pension as pension
from . import gosuslugi as gosuslugi

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=["start"])
async def send_welcome(message):
    await message.answer(
        "Добрый день, коллеги!\n\n"
        "С помощью чат-бота постараемся ответить на "
        "самые популярные вопросы наших будущих пенсионеров.\n\n"
        "Выберите тему:",
        reply_markup=kb.main_markup,
    )


@dp.message_handler(TextFilter(equals=kb.PENSION_BUTTON))
async def send_pension_willingness(message):
    await message.answer(
        pension.PENSION_PERIOD,
        reply_markup=kb.pension_period_markup,
    )


@dp.message_handler(TextFilter(equals=kb.MONTH_PERIOD_BUTTON))
async def send_month_period(message):
    await message.answer(
        "Выберите раздел",
        reply_markup=kb.pension_option_markup,
    )


@dp.message_handler(TextFilter(equals=kb.DOCUMENTS_MADE))
async def send_documents_choice_positive(message):
    await message.answer(
        pension.PENSION_MOHTH_DOCUMENTS_DONE,
        reply_markup=kb.when_and_how_apply,
    )


@dp.message_handler(TextFilter(equals=kb.PFR_APPEAL_BUTTON))
async def send_ways_to_apply(message):
    await message.answer(
        pension.WAYS_TO_APPLY,
        reply_markup=kb.pension_option_markup,
    )


@dp.message_handler(TextFilter(equals=kb.WHEN_APPLY_BUTTON))
async def send_when_apply(message):
    photo = open("pfr_instruction/images/instruction.png", "rb")
    await message.reply_photo(photo)
    await message.answer(
        pension.WHEN_APPLY,
        reply_markup=kb.pension_option_markup,
    )


@dp.message_handler(TextFilter(equals=kb.DOCUMENTS_NOT_MADE))
async def send_documents_choice_negative(message):
    await message.answer(
        pension.PENSION_MOHTH_DOCUMENTS_NOT_DONE,
        reply_markup=kb.when_and_how_apply,
    )


@dp.message_handler(TextFilter(equals=kb.YEAR_PERIOD_BUTTON))
async def send_year_period(message):
    await message.answer(
        pension.PENSION_YEAR_PERIOD,
        reply_markup=kb.need_documents_markup,
    )


@dp.message_handler(TextFilter(equals=kb.NEED_DOCUMENTS_BUTTON))
async def send_need_documents(message):
    await message.answer(
        pension.NEED_DOCUMENTS,
        reply_markup=kb.pension_period_markup,
    )


@dp.message_handler(TextFilter(equals=kb.SCHEDULE_BUTTON))
async def send_schedule(message):
    await message.answer(
        pension.SCHEDULE,
        reply_markup=kb.need_documents_markup,
    )


@dp.message_handler(TextFilter(equals=kb.YEARLY_ATTENTION_BUTTON))
async def send_important_yearly_info(message):
    await message.answer(
        pension.YEARLY_ATTENTION,
        reply_markup=kb.need_documents_markup,
    )


@dp.message_handler(TextFilter(equals=kb.MONTH_ATTENTION_BUTTON))
async def send_important_month_info(message):
    await message.answer(
        pension.MONTH_ATTENTION,
        reply_markup=kb.pension_option_markup,
    )


@dp.message_handler(TextFilter(equals=kb.GOSUSLUGI_BUTTON))
async def send_gosuslugi_registration(message):
    await message.answer(
        "Выберите вариант регистрации",
        reply_markup=kb.gosuslugi_registration_markup,
    )


@dp.message_handler(TextFilter(equals=kb.MFC_REGISTRATION_BUTTON))
async def send_mfc_registration(message):
    await message.answer(
        gosuslugi.MFC_REGISTRATION,
        reply_markup=kb.gosuslugi_registration_markup,
    )


@dp.message_handler(TextFilter(equals=kb.MOBILE_BANK_APP_REGISTRATION_BUTTON))
async def send_mobile_bank_app_registration(message):
    await message.answer(
        gosuslugi.MOBILE_BANK_APP_REGISTRATION,
        reply_markup=kb.gosuslugi_registration_markup,
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


def main():
    """Основная функция, отвечающая за запуск бота."""
    executor.start_polling(dp, skip_updates=True)
