from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


BACK_BUTTON = "На главную"

PENSION_BUTTON = "Готовлюсь к пенсии. С чего начать?"
YEAR_PERIOD_BUTTON = "До пенсии остался год. Проверка документов."
NEED_DOCUMENTS_BUTTON = "Список документов"
SCHEDULE_BUTTON = "Часы приёма фронт-офиса"
YEARLY_ATTENTION_BUTTON = "Важная информация"
MONTH_ATTENTION_BUTTON = "Полезная информация"
MONTH_PERIOD_BUTTON = "До пенсии остался месяц. Подача заявления."
DOCUMENTS_MADE = "Да. И я сдавал документы на проверку заранее"
WHEN_APPLY_BUTTON = "Когда и как подать заявление через Госуслуги?"
PFR_APPEAL_BUTTON = "Обращение в клиентскую службу ПФР"
ACROSS_GOSUSLUGI = "Через личный кабинет на сайте Госуслуги"
ACROSS_CLIENT_SERVICE = "Через клиентскую службу ПФР"
DOCUMENTS_NOT_MADE = "Да. Но я не сдавал документы на проверку заранее"

EXPERIENCE_BUTTON = "Как узнать свой стаж на сайте Госуслуг?"
GOSUSLUGI_BUTTON = "Госуслуги. Как зарегистрироваться?"
MFC_REGISTRATION_BUTTON = "Через МФЦ"
MOBILE_BANK_APP_REGISTRATION_BUTTON = "Через мобильное приложение банка"
USEFUL_GOSUSLUGI_INFO_BUTTON = ""


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
)

pension_option_markup = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(WHEN_APPLY_BUTTON))
    .add(KeyboardButton(PFR_APPEAL_BUTTON))
    .add(KeyboardButton(MONTH_ATTENTION_BUTTON))
    .add(KeyboardButton(BACK_BUTTON))
)

statement_pension_markup = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(ACROSS_GOSUSLUGI))
    .add(KeyboardButton(ACROSS_CLIENT_SERVICE))
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
