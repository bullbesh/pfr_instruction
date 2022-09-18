"""Основной модуль проекта, объединяющий в себе весь функционал бота 
и отображающий пользователю следующую информацию:

- "Готовлюсь к пенсии. С чего начать?"
- "Госуслуги. Как зарегистрироваться?"
- "Как узнать свой стаж на сайте Госуслуг?"
- "Куда обратиться за помощью?"

Для удобной навигации по сообщениям бота к каждой переменной прилагается 
комментарий.
"""

import logging
import os
from typing import List

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.message import Message

from textode import (
    BackNode,
    FuncNode,
    ImageNode,
    KeyboardNode,
    MultiNode,
    Node,
    NodeDict,
    TextNode,
    TO_MAIN,
)


from . import gosuslugi as gosuslugi
from . import keyboard as kb
from . import pension as pension


logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(lambda _: True)
async def handle_text(message: Message):
    """Обработчик всех текстовых сообщений."""
    node = NodeDict.get_node(message.text)
    if node is None:
        await message.answer(
            "Внимание! Чат-бот предлагает ГОТОВЫЕ вопросы и ответы. "
            "Не надо писать ему своих сообщений, просто выбирайте нужную кнопку."
        )
    else:
        await handle_node(node, message)


async def handle_node(node: Node, message: Message):
    if isinstance(node, MultiNode):
        for node in node.nodes:
            await handle_node(node, message)
    elif isinstance(node, (FuncNode, TextNode)):
        await message.answer(node.text)
    elif isinstance(node, KeyboardNode):
        keyboard = make_keyboard(node.buttons)
        await message.answer(node.text, reply_markup=keyboard)
    elif isinstance(node, BackNode):
        keyboard = make_keyboard(node.get_node_to_back().buttons)
        await message.answer(node.text, reply_markup=keyboard)
    elif isinstance(node, ImageNode):
        with open(node.path, mode="rb") as image:
            await message.answer_photo(image, caption=node.caption)


def make_keyboard(node_buttons: List[Node]) -> ReplyKeyboardMarkup:
    """Создание клавиатуры с помощью кнопок KeyboardNode."""
    return ReplyKeyboardMarkup(
        [[KeyboardButton(text=node.title)] for node in node_buttons],
        resize_keyboard=True,
    )


# Часы работа фронт-офиса.
schedule = TextNode(
    title=kb.SCHEDULE_BUTTON,
    text=pension.SCHEDULE,
)


# Список документов.
need_documents = TextNode(
    title=kb.NEED_DOCUMENTS_BUTTON,
    text=pension.NEED_DOCUMENTS,
)


# Важная информация.
yearly_attention = TextNode(
    title=kb.YEARLY_ATTENTION_BUTTON,
    text=pension.YEARLY_ATTENTION,
)


# До пенсии остался год. Проверка документов.
year_period = KeyboardNode(
    title=kb.YEAR_PERIOD_BUTTON,
    text=pension.PENSION_YEAR_PERIOD,
    buttons=[
        schedule,
        need_documents,
        yearly_attention,
        BackNode(kb.BACK_BUTTON, text="Воспользуйтесь клавиатурой", level=TO_MAIN),
    ],
)


# Когда и как подать заявление через Госуслуги?
when_apply = TextNode(
    title=kb.WHEN_APPLY_BUTTON,
    text=pension.WHEN_APPLY,
)


# Обращение в клиентскую службу ПФР.
pfr_appeal = TextNode(
    title=kb.PFR_APPEAL_BUTTON,
    text=pension.WAYS_TO_APPLY,
)


# Полезная информация.
month_attention = TextNode(
    title=kb.MONTH_ATTENTION_BUTTON,
    text=pension.MONTH_ATTENTION,
)


# До пенсии остался месяц. Подача заявления.
month_period = KeyboardNode(
    title=kb.MONTH_PERIOD_BUTTON,
    text="Выберите раздел",
    buttons=[
        when_apply,
        pfr_appeal,
        month_attention,
        BackNode(kb.BACK_BUTTON, text="Воспользуйтесь клавиатурой", level=TO_MAIN),
    ],
)


# Готовлюсь к пенсии. С чего начать?
pension_period = KeyboardNode(
    title=kb.PENSION_BUTTON,
    text=(
        "ЭТАПЫ ВЫХОДА НА ПЕНСИЮ:\n"
        "1. За один-два года до пенсии сдайте свои документы на проверку в ПФР "
        "(через Фронт-офис на ул. Жукова, 4)\n"
        "2. В течение месяца до пенсии отправьте заявление через госуслуги\n"
        "3. Получите в ПФР свидетельство пенсионера и справку о пенсии\n"
        "4. Справку о пенсии предоставьте своему менеджеру по "
        "персоналу или на ул. Жукова, 4 (каб. 1.19 или 3.14)\n\n"
        "Выберите интересующий вас период до пенсии"
    ),
    buttons=[
        year_period,
        month_period,
        need_documents,
        BackNode(kb.BACK_BUTTON, text="Воспользуйтесь клавиатурой", level=TO_MAIN),
    ],
)


# (регистрация) Через МФЦ.
mfc_registration = TextNode(
    title=kb.MFC_REGISTRATION_BUTTON,
    text=gosuslugi.MFC_REGISTRATION,
)


# (регистрация) Через мобильное приложение банка.
mobile_bank_app_registration = TextNode(
    title=kb.MOBILE_BANK_APP_REGISTRATION_BUTTON,
    text=gosuslugi.MOBILE_BANK_APP_REGISTRATION,
)


# Госуслуги. Как зарегистрироваться?
gosuslugi_registration = KeyboardNode(
    title=kb.GOSUSLUGI_BUTTON,
    text="Выберите вариант регистрации",
    buttons=[
        mfc_registration,
        mobile_bank_app_registration,
        BackNode(kb.BACK_BUTTON, text="Воспользуйтесь клавиатурой", level=TO_MAIN),
    ],
)


# Что такое Индивидуальный Лицевой Счёт? (выписка о стаже).
ils_explanation = TextNode(
    title=kb.ILS_EXPLANATION_BUTTON,
    text=gosuslugi.ILS_EXPLANATION,
)


# Как понимать выписку ИЛС?
ils_discharge_guide = MultiNode(
    title=(_ := kb.ILS_DISCHARGE_GUIDE_BUTTON),
    nodes=[
        ImageNode(_, path="pfr_instruction/images/ILSUnderstand.png"),
        TextNode(_, text=gosuslugi.ILS_DISCHARGE_GUIDE),
    ],
)


# Что делать, если в ИЛС нет данных о работе до 2002 года?
about_2002_works = TextNode(
    title=kb.ABOUT_2002_WORKS_BUTTON,
    text=gosuslugi.ABOUT_2002_WORKS,
)


# Куда обратиться по пенсионным вопросам?
contact_info = TextNode(
    title=kb.CONTACT_INFO_BUTTON,
    text=gosuslugi.CONTACT_INFO,
)


# Порядок обращения за выпиской ИЛС.
ils_appeal_order = ImageNode(
    title=kb.ILS_APPEAL_ORDER_BUTTON,
    path="pfr_instruction/images/OrderSearch.png",
    caption=gosuslugi.ILS_APPEAL_GUIDE,
)


# Как узнать свой стаж на сайте Госуслуг?
gosuslugi_experience = KeyboardNode(
    title=kb.EXPERIENCE_BUTTON,
    text="Задайте интересующий вас вопрос",
    buttons=[
        ils_explanation,
        ils_appeal_order,
        ils_discharge_guide,
        about_2002_works,
        contact_info,
        BackNode(kb.BACK_BUTTON, text="Воспользуйтесь клавиатурой", level=TO_MAIN),
    ],
)


# Начальная клавиатура.
main_node = KeyboardNode(
    title="/start",
    text=(
        "Добрый день, коллеги!\nЧат-бот постарается ответить на самые "
        "популярные вопросы наших сотрудников, готовящихся к выходу на пенсию. "
        "Нажмите на интересующую Вас тему.\n\nВнимание! Чат-бот предлагает "
        "ГОТОВЫЕ вопросы и ответы. Не надо писать ему своих сообщений, "
        "просто выбирайте нужную кнопку."
    ),
    buttons=[
        pension_period,
        gosuslugi_registration,
        gosuslugi_experience,
        contact_info,
    ],
)


def main():
    """Запуск бота."""
    executor.start_polling(dp, skip_updates=True)
