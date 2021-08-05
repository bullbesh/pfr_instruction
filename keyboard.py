from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


UNDERSTAND_BUTTON = 'Понятно'
BACK_BUTTON = 'На главную'

PENSION_BUTTON = 'Я готовлюсь к пенсии'
YEAR_PERIOD_BUTTON = 'Остался год до пенсии'
NEED_DOCUMENTS_BUTTON = 'Список документов'
SCHEDULE_BUTTON = 'Часы приёма'
MONTH_PERIOD_BUTTON = 'Через месяц пенсия'
DOCUMENTS_MADE = 'Подача заявления, документы проверены'
ACROSS_GOSUSLUGI = 'Через личный кабинет на сайте Госуслуги'
ACROSS_CLIENT_SERVICE = 'Через клиентскую службу ПФР'
DOCUMENTS_NOT_MADE = 'Подача заявления, документы НЕ проверялись'

EXPERIENCE_BUTTON = 'Как узнать, сколько у меня стажа'
GOSUSLUGI_BUTTON = 'Как зарегистироваться на Госуслугах'


agree_markup = (
	ReplyKeyboardMarkup(resize_keyboard=True)
	.add(KeyboardButton(UNDERSTAND_BUTTON))
)

main_markup = (
	ReplyKeyboardMarkup(resize_keyboard=True)
	.add(KeyboardButton(PENSION_BUTTON))
	.add(KeyboardButton(EXPERIENCE_BUTTON))
	.add(KeyboardButton(GOSUSLUGI_BUTTON))
)

pension_period_markup = (
	ReplyKeyboardMarkup(resize_keyboard=True)
	.add(KeyboardButton(YEAR_PERIOD_BUTTON))
	.add(KeyboardButton(MONTH_PERIOD_BUTTON))
)

pension_documents_markup = (
	ReplyKeyboardMarkup(resize_keyboard=True)
	.add(KeyboardButton(DOCUMENTS_MADE))
	.add(KeyboardButton(DOCUMENTS_NOT_MADE))
)

statement_pension_markup = (
	ReplyKeyboardMarkup(resize_keyboard=True)
	.add(KeyboardButton(ACROSS_GOSUSLUGI))
	.add(KeyboardButton(ACROSS_CLIENT_SERVICE))
)

need_documents_markup = (
	ReplyKeyboardMarkup(resize_keyboard=True)
	.row(
		KeyboardButton(NEED_DOCUMENTS_BUTTON),
		KeyboardButton(SCHEDULE_BUTTON)
	)
	.add(KeyboardButton(BACK_BUTTON))
)