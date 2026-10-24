# Деплой Telegram бота на Bothost

Этот репозиторий содержит Telegram-бота для подбора РКО-банка, готового к деплою на Bothost (bothost.ru).

## Стек
- Python 3.11
- aiogram 3.17.0
- MemoryStorage для FSM (подходит для 256MB RAM)

## Структура
```
bot/
├── main.py          # Основной файл бота
├── run.py           # Альтернативный запуск
├── handlers/        # Обработчики сообщений
├── keyboards/       # Клавиатуры
├── services/        # Логика рекомендаций
└── data/            # Данные о банках
```

## Локальный запуск

1. Скопируйте пример переменных окружения:
   ```bash
   cp .env.example .env
   ```

2. Вставьте ваш токен от @BotFather в `.env`:
   ```
   BOT_TOKEN=ваш_токен
   ```

3. Создайте виртуальное окружение и установите зависимости:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Linux/Mac
   pip install -r requirements.txt
   ```

4. Запустите бота:
   ```bash
   python main.py
   ```

## Деплой на Bothost (Free тариф)

### Подготовка
1. Убедитесь, что все изменения закоммичены:
   ```bash
   git add .
   git commit -m "Подготовка к деплою на Bothost"
   ```

2. Создайте публичный репозиторий на GitHub и добавьте remote:
   ```bash
   git remote add origin https://github.com/ваш-username/ваш-репозиторий.git
   git push -u origin main
   ```

### Настройка на Bothost
1. Перейдите на [bothost.ru](https://bothost.ru)
2. Создайте нового бота → Telegram
3. Вставьте токен от @BotFather в поле "Bot Token"
4. Укажите Git URL вашего репозитория
5. Выберите ветку `main`
6. Bothost автоматически определит Python по `requirements.txt`
7. Точка входа: `main.py` (указано в `bothost.json`)

### Важные моменты
- **Free тариф использует Long Polling** — бот уже настроен на этот режим
- **Токен задаётся в панели Bothost** → приходит как `BOT_TOKEN` в переменных окружения
- **Не запускайте бота локально с тем же токеном**, пока он работает на Bothost (Conflict: getUpdates)
- **Логирование**: все логи выводятся в stdout, доступны в панели Bothost
- **Память**: 256MB достаточно, используется MemoryStorage, нет тяжёлых зависимостей

## Проверка работы
После деплоя:
1. Дождитесь логов "Bot starting (polling)..."
2. Напишите боту `/start` в Telegram
3. Пройдите опрос для проверки функциональности

## Устранение неполадок
- **"BOT_TOKEN is not set"**: проверьте, что токен указан в панели Bothost
- **Конфликт обновлений**: остановите локальный бот перед деплоем
- **Логи не отображаются**: проверьте уровень логирования (по умолчанию INFO)

## Файлы конфигурации
- `bothost.json` — конфигурация для Bothost (точка входа, версия Python)
- `.env.example` — шаблон переменных окружения
- `requirements.txt` — зависимости Python

## Безопасность
- Никогда не коммитьте `.env` с реальным токеном
- Используйте `.env.example` как шаблон
- Токен хранится только в панели Bothost и локальном `.env`