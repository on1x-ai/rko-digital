import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    try:
        # Чтение токена из переменных окружения
        TOKEN = os.getenv("BOT_TOKEN") or os.getenv("TELEGRAM_BOT_TOKEN")
        if not TOKEN:
            raise RuntimeError("BOT_TOKEN is not set")
        
        logger.info("Bot starting (polling)...")
        
        bot = Bot(
            token=TOKEN,
            default=DefaultBotProperties(parse_mode="HTML")
        )
        
        # Проверяем подключение
        me = await bot.get_me()
        logger.info(f"Бот успешно подключен: @{me.username} ({me.first_name})")
        
        # Инициализируем диспетчер
        storage = MemoryStorage()
        dp = Dispatcher(storage=storage)
        
        # Импортируем роутеры
        from handlers.survey import router as survey_router
        dp.include_router(survey_router)
        
        logger.info("Бот запущен и готов к работе!")
        await dp.start_polling(bot)
        
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
        logger.info("Проверьте:")
        logger.info("1. Интернет-подключение")
        logger.info("2. Корректность токена")
        logger.info("3. Доступность Telegram API в вашем регионе")
        raise

if __name__ == "__main__":
    asyncio.run(main())