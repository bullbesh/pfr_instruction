"""Module containing constants and keyboards displayed by
the bot through main.py file.
"""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


BACK_BUTTON = "На главную"

PENSION_BUTTON = "Готовлюсь к пенсии. С чего начать?"
NEED_DOCUMENTS_BUTTON = "Список документов"
YEAR_PERIOD_BUTTON = "До пенсии остался год. Проверка документов."
SCHEDULE_BUTTON = "Часы приёма фронт-офиса"
YEARLY_ATTENTION_BUTTON = "Важная информация"

MONTH_PERIOD_BUTTON = "До пенсии остался месяц. Подача заявления."
WHEN_APPLY_BUTTON = "Когда и как подать заявление через Госуслуги?"
PFR_APPEAL_BUTTON = "Обращение в клиентскую службу ПФР"
MONTH_ATTENTION_BUTTON = "Полезная информация"

GOSUSLUGI_BUTTON = "Госуслуги. Как зарегистрироваться?"
MFC_REGISTRATION_BUTTON = "Через МФЦ"
MOBILE_BANK_APP_REGISTRATION_BUTTON = "Через мобильное приложение банка"

EXPERIENCE_BUTTON = "Как узнать свой стаж на сайте Госуслуг?"
ILS_EXPLANATION_BUTTON = "Что такое Индивидуальный лицевой счёт?"
ILS_DISCHARGE_DESTINY_BUTTON = "Зачем нужна выписка из ИЛС?"
ILS_DISCHARGE_GUIDE_BUTTON = "Как понимать выписку ИЛС?"
ABOUT_2002_WORKS_BUTTON = (
    "Что делать, если в ИЛС нет данных о работе до 2002 года?"
)
CONTACT_INFO_BUTTON = "Куда обратиться по пенсионным вопросам?"


main_markup = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(PENSION_BUTTON))
    .add(KeyboardButton(GOSUSLUGI_BUTTON))
    .add(KeyboardButton(EXPERIENCE_BUTTON))
)

pension_period_markup = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(YEAR_PERIOD_BUTTON))
    .add(KeyboardButton(MONTH_PERIOD_BUTTON))
    .add(KeyboardButton(NEED_DOCUMENTS_BUTTON))
    .add(KeyboardButton(BACK_BUTTON))
)

pension_option_markup = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(WHEN_APPLY_BUTTON))
    .add(KeyboardButton(PFR_APPEAL_BUTTON))
    .add(KeyboardButton(MONTH_ATTENTION_BUTTON))
    .add(KeyboardButton(BACK_BUTTON))
)

need_documents_markup = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .row(
        KeyboardButton(SCHEDULE_BUTTON),
        KeyboardButton(YEARLY_ATTENTION_BUTTON),
    )
    .add(KeyboardButton(BACK_BUTTON))
)

when_and_how_apply = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(MONTH_PERIOD_BUTTON))
    .add(KeyboardButton(WHEN_APPLY_BUTTON))
    .add(KeyboardButton(PFR_APPEAL_BUTTON))
)

gosuslugi_registration_markup = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(MFC_REGISTRATION_BUTTON))
    .add(KeyboardButton(MOBILE_BANK_APP_REGISTRATION_BUTTON))
    .add(KeyboardButton(BACK_BUTTON))
)

gosuslugi_experience_markup = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(ILS_EXPLANATION_BUTTON))
    .add(KeyboardButton(ILS_DISCHARGE_DESTINY_BUTTON))
    .add(KeyboardButton(ILS_DISCHARGE_GUIDE_BUTTON))
    .add(KeyboardButton(ABOUT_2002_WORKS_BUTTON))
    .add(KeyboardButton(CONTACT_INFO_BUTTON))
    .add(KeyboardButton(BACK_BUTTON))
)
