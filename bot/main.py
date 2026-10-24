import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from handlers.survey import router as survey_router


# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def main():
    """Основная функция запуска бота"""
    # Чтение токена из переменных окружения
    TOKEN = os.getenv("BOT_TOKEN") or os.getenv("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is not set")
    
    # Инициализация бота и диспетчера
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode="HTML")
    )
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # Регистрация роутеров
    dp.include_router(survey_router)
    
    logger.info("Bot starting (polling)...")
    
    # Запуск поллинга
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())