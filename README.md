# Telegram Utility Bot

Простой Telegram-бот на Python с базовыми командами и интерактивными кнопками.

## Возможности

* `/start` — приветствие и запуск бота
* `/help` — справочная информация
* `/about` — информация о проекте
* `/menu` — интерактивное меню
* Кнопка «О проекте»
* Кнопка «Помощь»
* Кнопка «Мой ID»
* Echo-режим — бот повторяет сообщения пользователя

## Технологии

* Python 3.12+
* aiogram 3
* python-dotenv
* Telegram Bot API

## Запуск

1. Установить зависимости:

```bash
pip install -r requirements.txt
```

2. Создать файл `.env` и добавить токен Telegram-бота:

```env
BOT_TOKEN=your_bot_token
```

3. Запустить бота:

```bash
python bot.py
```

## Структура проекта

```text
telegram-utility-bot/
├── bot.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

> Файл `.env` не публикуется в GitHub и используется только локально для хранения токена бота.

## Статус

Учебный портфолио-проект, созданный для практики разработки Telegram-ботов на Python и aiogram.
