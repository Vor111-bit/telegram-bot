import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Включаем логирование (поможет отслеживать ошибки)
logging.basicConfig(level=logging.INFO)

# Получаем токен бота из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я бот для прогнозов на спорт!")

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(f"Ты написал: {message.text}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
