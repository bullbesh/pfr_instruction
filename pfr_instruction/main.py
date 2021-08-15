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
        "Добрый день!\n\n"
        "Вы готовитесь к пенсии?\n"
        "Или хотите узнать сколько у вас стажа?\n"
        "Как быстро зарегистрироваться на Госуслугах?\n\n"
        "Наш чат-бот подскажет, как это сделать. Начнём?",
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
        "Выберите раздел",
        reply_markup=kb.pension_option_markup,
    )


@dp.message_handler(TextFilter(equals=kb.WHEN_APPLY_BUTTON))
async def send_month_period(message):
    from pension import WHEN_APPLY

    await message.answer(
        WHEN_APPLY,
        reply_markup=kb.pension_option_markup,
    )


@dp.message_handler(TextFilter(equals=kb.DOCUMENTS_MADE))
async def send_documents_choice_positive(message):
    from pension import PENSION_MOHTH_DOCUMENTS_DONE

    await message.answer(
        PENSION_MOHTH_DOCUMENTS_DONE,
        reply_markup=kb.when_and_how_apply,
    )


@dp.message_handler(TextFilter(equals=kb.HOW_APPLY_BUTTON))
async def send_ways_to_apply(message):
    from pension import WAYS_TO_APPLY

    await message.answer(
        WAYS_TO_APPLY,
        reply_markup=kb.pension_option_markup,
    )


@dp.message_handler(TextFilter(equals=kb.WHEN_APPLY_BUTTON))
async def send_when_apply(message):
    from pension import WHEN_APPLY

    await message.answer(
        WHEN_APPLY,
        reply_markup=kb.main_markup,
    )


@dp.message_handler(TextFilter(equals=kb.DOCUMENTS_NOT_MADE))
async def send_documents_choice_negative(message):
    from pension import PENSION_MOHTH_DOCUMENTS_NOT_DONE

    await message.answer(
        PENSION_MOHTH_DOCUMENTS_NOT_DONE,
        reply_markup=kb.when_and_how_apply,
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


@dp.message_handler(TextFilter(equals=kb.YEARLY_ATTENTION_BUTTON))
async def send_important_yearly_info(message):
    from pension import YEARLY_ATTENTION

    await message.answer(
        YEARLY_ATTENTION,
        reply_markup=kb.need_documents_markup,
    )


@dp.message_handler(TextFilter(equals=kb.MONTH_ATTENTION_BUTTON))
async def send_important_month_info(message):
    from pension import MONTH_ATTENTION

    await message.answer(
        MONTH_ATTENTION,
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
    from gosuslugi import MFC_REGISTRATION

    await message.answer(
        MFC_REGISTRATION,
        reply_markup=kb.gosuslugi_registration_markup,
    )


@dp.message_handler(TextFilter(equals=kb.MOBILE_BANK_APP_REGISTRATION_BUTTON))
async def send_mobile_bank_app_registration(message):
    from gosuslugi import MOBILE_BANK_APP_REGISTRATION

    await message.answer(
        MOBILE_BANK_APP_REGISTRATION,
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


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
