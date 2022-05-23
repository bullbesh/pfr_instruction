# **PFR Instruction** — бот для предприятия «Северсталь».
Информация о пенсии и всём, что с ней связано.

## Предназначение
Помощь сотрудникам отдела по пенсионным вопросам, обучение новых работников.

## Разделы бота
В общей сложности бот имеет три основных раздела с функциями, которые включают полезную информацию:
- Подготовка к пенсии
- Стаж работника предприятия
- Сайт "Госуслуги"

```mermaid
flowchart TD;
    Main["Приветствие"];
    PensionPeriod["Готовлюсь к пенсии. С чего начать?"];
    GosuslugiRegistration["Госyслуги. Как зарегистрироваться?"];
    GosuslugiExperience["Как узнать свой стаж на сайте Госуслуг?"];
    ContactInfo["Куда обратиться по пенсионным вопросам?"];

    YearPeriod["До пенсии остался год. Проверка документов"];
    MonthPeriod["До пенсии остался месяц. Подача заявления"];
    NeedDocuments["Список документов"];

    MFCRegistrarion["Через МФЦ"];
    MobileBankAppRegistration["Через мобильное приложение банка"];

    ILSExplanation["Что такое Индивидуальный лицевой счёт?"];
    ILSAppealOrder["Порядок обращения за выпиской ИЛС"];
    ILSDischargeGuide["Как понимать выписку ИЛС?"];
    About2002Works["Что делать, если в ИЛС нет данных о работе до 2002 года?"];

    Schedule["Часы работы Фронт-офиса"];
    YearlyAttention["Важная информация"];

    WhenApply["Когда и как подать заявление через Госуслуги?"];
    PFRAppeal["Обращение в клиентскую службу ПФР"];
    MonthAttention["Полезная информация"];



    Main --> PensionPeriod;
    Main --> GosuslugiRegistration;
    Main --> GosuslugiExperience;
    Main --> ContactInfo;

    PensionPeriod --> MonthPeriod;
    PensionPeriod --> YearPeriod;
    PensionPeriod --> NeedDocuments;

    GosuslugiRegistration --> MFCRegistrarion;
    GosuslugiRegistration --> MobileBankAppRegistration;

    GosuslugiExperience --> ILSExplanation;
    GosuslugiExperience --> ILSAppealOrder;
    GosuslugiExperience --> ILSDischargeGuide;
    GosuslugiExperience --> About2002Works;
    GosuslugiExperience --> ContactInfo;

    YearPeriod --> Schedule;
    YearPeriod --> NeedDocuments;
    YearPeriod --> YearlyAttention;

    MonthPeriod --> WhenApply;
    MonthPeriod --> PFRAppeal;
    MonthPeriod --> MonthAttention;
    
```

## Как пользоваться ботом
Адрес бота в Telegram: [@pfrinstruction_bot](https://t.me/pfrinstruction_bot)

Весь процесс общения построен на принципе «вопрос-ответ». 
Напишите боту в личные сообщения и выберите на клавиатуре кнопку с 
интересующим Вас вопросом.

## Реализация проекта
- Библиотека для работы с Telegram - [aiogram](https://github.com/aiogram/aiogram)
- Иерархия построения сообщений бота - [textode](https://github.com/Masynchin/textode)
- Облачное хранилище для автономной работы проекта - [heroku](https://heroku.com)

## Лицензия
[MIT](https://github.com/bullbesh/pfr_instruction/blob/main/license.md)
