from aiogram.fsm.state import State, StatesGroup


class SurveyStates(StatesGroup):
    """Состояния опроса"""
    business_status = State()  # Q1. Статус бизнеса
    business_field = State()   # Q2. Сфера
    monthly_turnover = State() # Q3. Оборот
    foreign_payments = State() # Q4. Иностранные клиенты/валюта
    priority = State()         # Q5. Что важнее сейчас
    need_acquiring = State()   # Q6. Эквайринг/карты (опционально)
    ready_to_register = State() # Q7. Готовы оформить ИП/ООО (только если Q1 = Нет)