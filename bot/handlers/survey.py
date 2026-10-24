from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode

from handlers.states import SurveyStates
from keyboards.survey import (
    get_main_menu, get_survey_keyboard, get_restart_keyboard, get_offer_keyboard,
    BUSINESS_STATUS_BUTTONS, BUSINESS_FIELD_BUTTONS, TURNOVER_BUTTONS,
    FOREIGN_PAYMENTS_BUTTONS, PRIORITY_BUTTONS, ACQUIRING_BUTTONS, REGISTER_READY_BUTTONS
)
from services.recommend import UserAnswers, recommend_bank, format_recommendation

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    """Обработчик команды /start"""
    welcome_text = (
        "👋 *Привет!*\n\n"
        "Я помогу подобрать расчётный счёт для digital-бизнеса.\n\n"
        "Ответьте на несколько коротких вопросов — предложу банк под вашу задачу и дам ссылку на открытие.\n\n"
        "📌 *Почту указывать не нужно.*"
    )
    await message.answer(welcome_text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_main_menu())


@router.message(F.text == "ℹ️ Как это работает")
async def how_it_works(message: Message):
    """Информация о работе бота"""
    info_text = (
        "🤔 *Как это работает:*\n\n"
        "1. Вы отвечаете на 5–7 простых вопросов о бизнесе\n"
        "2. Я анализирую вашу ситуацию по чётким правилам\n"
        "3. Рекомендую 1 основной банк (+ запасной при необходимости)\n"
        "4. Даю партнёрскую ссылку для открытия счёта\n\n"
        "💡 *Важно:*\n"
        "• Не спрашиваю email и телефон\n"
        "• Не обещаю «100% одобрение»\n"
        "• Рекомендую только проверенные банки\n\n"
        "🎯 *Начнём?*"
    )
    await message.answer(info_text, parse_mode=ParseMode.MARKDOWN, reply_markup=get_main_menu())


@router.message(F.text == "🎯 Подобрать банк")
async def start_survey(message: Message, state: FSMContext):
    """Начало опроса"""
    await state.set_state(SurveyStates.business_status)
    question = (
        "📋 *Вопрос 1 из 7*\n\n"
        "У вас уже есть ИП или ООО?"
    )
    await message.answer(
        question,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=get_survey_keyboard(BUSINESS_STATUS_BUTTONS, columns=1)
    )


@router.message(SurveyStates.business_status)
async def process_business_status(message: Message, state: FSMContext):
    """Обработка статуса бизнеса"""
    if message.text not in BUSINESS_STATUS_BUTTONS:
        await message.answer("Пожалуйста, выберите вариант из предложенных:")
        return
    
    # Маппинг ответа на внутренний формат
    status_map = {
        "Да": "has_entity",
        "Нет, только планирую": "planning", 
        "Работаю как самозанятый (НПД)": "self_employed"
    }
    
    await state.update_data(business_status=status_map[message.text])
    
    # Переход к следующему вопросу
    await state.set_state(SurveyStates.business_field)
    question = (
        "📋 *Вопрос 2 из 7*\n\n"
        "Чем зарабатываете?"
    )
    await message.answer(
        question,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=get_survey_keyboard(BUSINESS_FIELD_BUTTONS)
    )


@router.message(SurveyStates.business_field)
async def process_business_field(message: Message, state: FSMContext):
    """Обработка сферы деятельности"""
    if message.text not in BUSINESS_FIELD_BUTTONS:
        await message.answer("Пожалуйста, выберите вариант из предложенных:")
        return
    
    # Маппинг ответа
    field_map = {
        "IT/разработка": "it",
        "Фриланс (дизайн, тексты, маркетинг)": "freelance",
        "Онлайн-школа или курсы": "online_school", 
        "Магазин": "shop",
        "Агентство": "agency",
        "Другое": "other"
    }
    
    await state.update_data(business_field=field_map[message.text])
    
    # Переход к следующему вопросу
    await state.set_state(SurveyStates.monthly_turnover)
    question = (
        "📋 *Вопрос 3 из 7*\n\n"
        "Какой оборот примерно в месяц?"
    )
    await message.answer(
        question,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=get_survey_keyboard(TURNOVER_BUTTONS)
    )


@router.message(SurveyStates.monthly_turnover)
async def process_monthly_turnover(message: Message, state: FSMContext):
    """Обработка оборота"""
    if message.text not in TURNOVER_BUTTONS:
        await message.answer("Пожалуйста, выберите вариант из предложенных:")
        return
    
    # Маппинг ответа
    turnover_map = {
        "до 100 тыс": "under_100k",
        "100–300 тыс": "100_300k",
        "300 тыс – 1 млн": "300k_1m", 
        "больше 1 млн": "over_1m",
        "Пока почти нет": "almost_none"
    }
    
    await state.update_data(monthly_turnover=turnover_map[message.text])
    
    # Переход к следующему вопросу
    await state.set_state(SurveyStates.foreign_payments)
    question = (
        "📋 *Вопрос 4 из 7*\n\n"
        "Есть оплаты из-за рубежа или в валюте?"
    )
    await message.answer(
        question,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=get_survey_keyboard(FOREIGN_PAYMENTS_BUTTONS)
    )


@router.message(SurveyStates.foreign_payments)
async def process_foreign_payments(message: Message, state: FSMContext):
    """Обработка иностранных платежей"""
    if message.text not in FOREIGN_PAYMENTS_BUTTONS:
        await message.answer("Пожалуйста, выберите вариант из предложенных:")
        return
    
    # Маппинг ответа
    foreign_map = {
        "Да, регулярно": "regular",
        "Иногда": "sometimes",
        "Нет, только РФ": "no"
    }
    
    await state.update_data(foreign_payments=foreign_map[message.text])
    
    # Переход к следующему вопросу
    await state.set_state(SurveyStates.priority)
    question = (
        "📋 *Вопрос 5 из 7*\n\n"
        "Что сейчас важнее?"
    )
    await message.answer(
        question,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=get_survey_keyboard(PRIORITY_BUTTONS)
    )


@router.message(SurveyStates.priority)
async def process_priority(message: Message, state: FSMContext):
    """Обработка приоритета"""
    if message.text not in PRIORITY_BUTTONS:
        await message.answer("Пожалуйста, выберите вариант из предложенных:")
        return
    
    # Маппинг ответа (новые короткие тексты для iPhone)
    priority_map = {
        "Подешевле на старте": "cheap",
        "Крупный банк": "reliable",
        "Всё онлайн": "simple",
        "Нужна валюта": "foreign"
    }
    
    await state.update_data(priority=priority_map[message.text])
    
    # Проверяем, нужно ли спрашивать эквайринг
    data = await state.get_data()
    
    # Для некоторых сфер эквайринг более релевантен
    relevant_for_acquiring = data.get('business_field') in ['shop', 'online_school', 'agency']
    
    if relevant_for_acquiring:
        await state.set_state(SurveyStates.need_acquiring)
        question = (
            "📋 *Вопрос 6 из 7*\n\n"
            "Нужен приём оплаты картами на сайте или по ссылке?"
        )
        await message.answer(
            question,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_survey_keyboard(ACQUIRING_BUTTONS)
        )
    else:
        # Пропускаем вопрос про эквайринг
        await process_skipped_acquiring(message, state)


async def process_skipped_acquiring(message: Message, state: FSMContext):
    """Пропуск вопроса про эквайринг"""
    data = await state.get_data()
    
    # Проверяем, нужно ли спрашивать про регистрацию
    if data.get('business_status') == 'planning':
        await state.set_state(SurveyStates.ready_to_register)
        question = (
            "📋 *Вопрос 6 из 7*\n\n"
            "Готовы оформить ИП/ООО сейчас?"
        )
        await message.answer(
            question,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_survey_keyboard(REGISTER_READY_BUTTONS)
        )
    else:
        # Завершаем опрос
        await finish_survey(message, state)


@router.message(SurveyStates.need_acquiring)
async def process_need_acquiring(message: Message, state: FSMContext):
    """Обработка вопроса про эквайринг"""
    if message.text not in ACQUIRING_BUTTONS:
        await message.answer("Пожалуйста, выберите вариант из предложенных:")
        return
    
    # Маппинг ответа
    acquiring_map = {
        "Да": "yes",
        "Нет": "no",
        "Позже": "later"
    }
    
    await state.update_data(need_acquiring=acquiring_map[message.text])
    
    # Проверяем, нужно ли спрашивать про регистрацию
    data = await state.get_data()
    if data.get('business_status') == 'planning':
        await state.set_state(SurveyStates.ready_to_register)
        question = (
            "📋 *Вопрос 7 из 7*\n\n"
            "Готовы оформить ИП/ООО сейчас?"
        )
        await message.answer(
            question,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_survey_keyboard(REGISTER_READY_BUTTONS)
        )
    else:
        # Завершаем опрос
        await finish_survey(message, state)


@router.message(SurveyStates.ready_to_register)
async def process_ready_to_register(message: Message, state: FSMContext):
    """Обработка готовности регистрировать бизнес"""
    if message.text not in REGISTER_READY_BUTTONS:
        await message.answer("Пожалуйста, выберите вариант из предложенных:")
        return
    
    # Маппинг ответа
    register_map = {
        "Да, хочу с регистрацией": "yes",
        "Нет, сначала разберусь сам": "no"
    }
    
    await state.update_data(ready_to_register=register_map[message.text])
    
    # Завершаем опрос
    await finish_survey(message, state)


async def finish_survey(message: Message, state: FSMContext):
    """Завершение опроса и вывод рекомендации"""
    # Получаем все данные
    data = await state.get_data()
    
    # Логируем ответы
    import logging
    logger = logging.getLogger(__name__)
    logger.info(f"User {message.from_user.id} answers: {data}")
    
    # Создаем объект ответов
    answers = UserAnswers(
        business_status=data.get('business_status'),
        business_field=data.get('business_field'),
        monthly_turnover=data.get('monthly_turnover'),
        foreign_payments=data.get('foreign_payments'),
        priority=data.get('priority'),
        need_acquiring=data.get('need_acquiring'),
        ready_to_register=data.get('ready_to_register')
    )
    
    # Получаем рекомендацию
    recommendation = recommend_bank(answers)
    recommendation_text = format_recommendation(recommendation)
    
    # Отправляем рекомендацию
    await message.answer(
        "🎉 *Готово!*\n\nВот моя рекомендация:\n",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=get_restart_keyboard()
    )
    
    # Отправляем рекомендацию с инлайн-кнопками
    await message.answer(
        recommendation_text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=get_offer_keyboard(recommendation.main_url, recommendation.backup_url),
        disable_web_page_preview=True
    )
    
    # Очищаем состояние
    await state.clear()


@router.message(F.text == "🔄 Пройти ещё раз")
async def restart_survey(message: Message, state: FSMContext):
    """Перезапуск опроса"""
    await start_survey(message, state)


@router.message(F.text == "🏠 В главное меню")
async def back_to_main(message: Message, state: FSMContext):
    """Возврат в главное меню"""
    await state.clear()
    await cmd_start(message)


@router.message()
async def handle_other_messages(message: Message):
    """Обработка других сообщений"""
    await message.answer(
        "Используйте кнопки меню или команды:\n"
        "/start — начать сначала\n"
        "🎯 Подобрать банк — начать опрос",
        reply_markup=get_main_menu()
    )