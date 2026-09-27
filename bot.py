import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("Не найден BOT_TOKEN. Добавь его в файл .env")

bot = Bot(token=TOKEN)
dp = Dispatcher()


def menu_keyboard() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="О проекте", callback_data="about")],
            [types.InlineKeyboardButton(text="Помощь", callback_data="help")],
            [types.InlineKeyboardButton(text="Мой ID", callback_data="my_id")],
        ]
    )

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Я эхо-бот.")

@dp.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer("Доступные команды\n/start - приветствие\n/help - помощь\n/about - о боте")

@dp.message(Command("about"))
async def about_handler(message: types.Message):
    await message.answer("Я учебный бот.\nСоздан в 2026 году.\nУмею отвечать на команды и повторять текст.")


@dp.message(Command("menu"))
async def menu_handler(message: types.Message):
    await message.answer("Выбери пункт меню:", reply_markup=menu_keyboard())


@dp.callback_query(F.data == "about")
async def menu_about_callback(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Я учебный бот.\nСоздан в 2026 году.\nУмею отвечать на команды и повторять текст.")


@dp.callback_query(F.data == "help")
async def menu_help_callback(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Доступные команды\n/start - приветствие\n/help - помощь\n/about - о боте\n/menu - меню")


@dp.callback_query(F.data == "my_id")
async def menu_id_callback(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"Твой ID: {callback.from_user.id}")


@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())