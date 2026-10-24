#!/usr/bin/env python3
"""
Точка входа для Bothost - запускает бота из папки bot
"""
import sys
import os

# Добавляем папку bot в путь
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'bot'))

# Импортируем и запускаем основной файл бота
if __name__ == "__main__":
    try:
        from main import main
        import asyncio
        asyncio.run(main())
    except Exception as e:
        print(f"Error starting bot: {e}")
        sys.exit(1)