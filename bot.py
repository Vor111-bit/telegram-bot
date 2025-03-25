import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram import Bot, Dispatcher


# Включаем логирование (поможет отслеживать ошибки)
logging.basicConfig(level=logging.INFO)

# Получаем токен бота из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

import os
bot = Bot(token=os.getenv("BOT_TOKEN"))  # Берём токен из Render

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я бот для прогнозов на спорт!")

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(f"Ты написал: {message.text}")

if __name__ == "__main__":
    async def main():
    bot = Bot(token="ТВОЙ_ТОКЕН")  # ✅ Теперь правильный отступ
    dp = Dispatcher()
    
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

