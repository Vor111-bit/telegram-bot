import asyncio
import os
from aiogram import Bot, Dispatcher

async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN"))  # ✅ Берём токен из переменных окружения
    dp = Dispatcher()

    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())  # Запускаем асинхронный цикл
