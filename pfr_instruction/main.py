"""The main module of the project, combining all the functionality of the bot
and displaying information to the user:

- Information about pension
- Work experience
- Gosuslugi website
"""

import logging
import os

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text as TextFilter

from . import gosuslugi as gosuslugi
from . import keyboard as kb
from . import pension as pension

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=["start"])
async def send_welcome(message):
    """Send a greeting with a short description of the bot."""
    await message.answer(
        "Добрый день, коллеги!\n\n"
        "С помощью чат-бота постараемся ответить на "
        "самые популярные вопросы наших будущих пенсионеров.\n\n"
        "Выберите тему, воспользовавшись кнопками на клавиатуре:",
        reply_markup=kb.main_markup,
    )


@dp.message_handler(TextFilter(equals=kb.PENSION_BUTTON))
async def send_pension_willingness(message):
    """Send a selection of one of two periods:

    - Monthly period
    - Yearly period
    """
    await message.answer(
        pension.PENSION_PERIOD,
        reply_markup=kb.pension_period_markup,
    )


@dp.message_handler(TextFilter(equals=kb.MONTH_PERIOD_BUTTON))
async def send_month_period_functions(message):
    """Send monthly period functions:

    - When and how to apply through Gosuslugi?
    - Contacting the PFR customer service
    - Useful information
    - Back
    """
    await message.answer(
        "Выберите раздел",
        reply_markup=kb.pension_option_markup,
    )


@dp.message_handler(TextFilter(equals=kb.PFR_APPEAL_BUTTON))
async def send_ways_to_apply(message):
    """Send contacting to the PFR customer service."""
    await message.answer(
        pension.WAYS_TO_APPLY,
        reply_markup=kb.pension_option_markup,
    )


@dp.message_handler(TextFilter(equals=kb.WHEN_APPLY_BUTTON))
async def send_when_apply(message):
    """Send information about when and how to
    apply through the Gosuslugi (with photo instruction).
    """
    photo = open("pfr_instruction/images/instruction.png", "rb")
    await message.reply_photo(photo)
    await message.answer(
        pension.WHEN_APPLY,
        reply_markup=kb.pension_option_markup,
    )


@dp.message_handler(TextFilter(equals=kb.YEAR_PERIOD_BUTTON))
async def send_year_period_functions(message):
    """Send yearly period functions:

    - Front Office Reception Hours
    - Useful information
    - Back
    """
    await message.answer(
        pension.PENSION_YEAR_PERIOD,
        reply_markup=kb.need_documents_markup,
    )


@dp.message_handler(TextFilter(equals=kb.NEED_DOCUMENTS_BUTTON))
async def send_need_documents(message):
    """Send a list of required documents."""
    await message.answer(
        pension.NEED_DOCUMENTS,
        reply_markup=kb.pension_period_markup,
    )


@dp.message_handler(TextFilter(equals=kb.SCHEDULE_BUTTON))
async def send_front_office_schedule(message):
    """Send a Front Office schedule."""
    await message.answer(
        pension.SCHEDULE,
        reply_markup=kb.need_documents_markup,
    )


@dp.message_handler(TextFilter(equals=kb.YEARLY_ATTENTION_BUTTON))
async def send_important_yearly_info(message):
    """Send important information about the yearly period."""
    await message.answer(
        pension.YEARLY_ATTENTION,
        reply_markup=kb.need_documents_markup,
    )


@dp.message_handler(TextFilter(equals=kb.MONTH_ATTENTION_BUTTON))
async def send_important_month_info(message):
    """Send important information about the monthly period."""
    await message.answer(
        pension.MONTH_ATTENTION,
        reply_markup=kb.pension_option_markup,
    )


@dp.message_handler(TextFilter(equals=kb.GOSUSLUGI_BUTTON))
async def send_gosuslugi_registration(message):
    """Send a selection of one of two registration types:

    - Via the MFC
    - Via the bank's mobile application
    """
    await message.answer(
        "Выберите вариант регистрации",
        reply_markup=kb.gosuslugi_registration_markup,
    )


@dp.message_handler(TextFilter(equals=kb.MFC_REGISTRATION_BUTTON))
async def send_mfc_registration(message):
    """Send instructions when registering through the MFC."""
    await message.answer(
        gosuslugi.MFC_REGISTRATION,
        reply_markup=kb.gosuslugi_registration_markup,
    )


@dp.message_handler(TextFilter(equals=kb.MOBILE_BANK_APP_REGISTRATION_BUTTON))
async def send_mobile_bank_app_registration(message):
    """Send instructions during registration
    via the bank's mobile application.
    """
    await message.answer(
        gosuslugi.MOBILE_BANK_APP_REGISTRATION,
        reply_markup=kb.gosuslugi_registration_markup,
    )


@dp.message_handler(TextFilter(equals=kb.BACK_BUTTON))
async def send_back(message):
    """Send the user to the main keyboard."""
    await message.answer(
        "Воспользуйтесь клавиатурой",
        reply_markup=kb.main_markup,
    )


@dp.message_handler()
async def send_error(message):
    """Send instructions in case of unrecognized message."""
    await message.answer(
        "Сообщение не распознано!\n\n"
        "Для вызова функций используйте навигационные кнопки ниже!",
    )
    await message.answer(
        "Перенос в главное меню...",
        reply_markup=kb.main_markup,
    )


def main():
    """Run bot."""
    executor.start_polling(dp, skip_updates=True)
