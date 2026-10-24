from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def get_main_menu() -> ReplyKeyboardMarkup:
    """Главное меню после /start"""
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="🎯 Подобрать банк"))
    builder.add(KeyboardButton(text="ℹ️ Как это работает"))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def get_survey_keyboard(buttons: list[str], columns: int = 2) -> ReplyKeyboardMarkup:
    """Клавиатура для опроса с кнопками"""
    builder = ReplyKeyboardBuilder()
    for button in buttons:
        builder.add(KeyboardButton(text=button))
    builder.adjust(columns)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def get_restart_keyboard() -> ReplyKeyboardMarkup:
    """Клавиатура после рекомендации"""
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="🔄 Пройти ещё раз"))
    builder.add(KeyboardButton(text="🏠 В главное меню"))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def get_offer_keyboard(main_url: str, backup_url: str = None) -> InlineKeyboardMarkup:
    """Инлайн-клавиатура с ссылками на офферы"""
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="📝 Открыть счёт", url=main_url))
    
    if backup_url:
        builder.add(InlineKeyboardButton(text="💡 Запасной вариант", url=backup_url))
    
    builder.adjust(1)
    return builder.as_markup()


# Тексты кнопок для опроса
BUSINESS_STATUS_BUTTONS = ["Да", "Нет, только планирую", "Работаю как самозанятый (НПД)"]
BUSINESS_FIELD_BUTTONS = ["IT/разработка", "Фриланс (дизайн, тексты, маркетинг)", "Онлайн-школа или курсы", "Магазин", "Агентство", "Другое"]
TURNOVER_BUTTONS = ["до 100 тыс", "100–300 тыс", "300 тыс – 1 млн", "больше 1 млн", "Пока почти нет"]
FOREIGN_PAYMENTS_BUTTONS = ["Да, регулярно", "Иногда", "Нет, только РФ"]
PRIORITY_BUTTONS = ["Подешевле на старте", "Крупный банк", "Всё онлайн", "Нужна валюта"]
ACQUIRING_BUTTONS = ["Да", "Нет", "Позже"]
REGISTER_READY_BUTTONS = ["Да, хочу с регистрацией", "Нет, сначала разберусь сам"]