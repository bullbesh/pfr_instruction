from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


UNDERSTAND_BUTTON = "Начнём!"
BACK_BUTTON = "На главную"

PENSION_BUTTON = "Я готовлюсь к пенсии"
YEAR_PERIOD_BUTTON = "Остался год до пенсии"
NEED_DOCUMENTS_BUTTON = "Список документов"
SCHEDULE_BUTTON = "Часы приёма"
YEARLY_ATTENTION_BUTTON = "Важная информация"
MONTH_ATTENTION_BUTTON = "Это полезно знать"
MONTH_PERIOD_BUTTON = "До пенсии остался месяц"
DOCUMENTS_MADE = "Да. И я сдавал документы на проверку заранее"
WHEN_APPLY_BUTTON = "Когда подавать заявление?"
HOW_APPLY_BUTTON = "Способы подачи заявления"
ACROSS_GOSUSLUGI = "Через личный кабинет на сайте Госуслуги"
ACROSS_CLIENT_SERVICE = "Через клиентскую службу ПФР"
DOCUMENTS_NOT_MADE = "Да. Но я не сдавал документы на проверку заранее"

EXPERIENCE_BUTTON = "Как можно узнать свой стаж?"
GOSUSLUGI_BUTTON = "Госуслуги. Как зарегистрироваться?"


agree_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(UNDERSTAND_BUTTON)
)

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
)

pension_option_markup = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(WHEN_APPLY_BUTTON))
    .add(KeyboardButton(HOW_APPLY_BUTTON))
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
    .row(KeyboardButton(NEED_DOCUMENTS_BUTTON),
        KeyboardButton(SCHEDULE_BUTTON),
        KeyboardButton(YEARLY_ATTENTION_BUTTON))
    .add(KeyboardButton(BACK_BUTTON))
)

when_and_how_apply = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton(MONTH_PERIOD_BUTTON))   
    .add(KeyboardButton(WHEN_APPLY_BUTTON))
    .add(KeyboardButton(HOW_APPLY_BUTTON))

)
