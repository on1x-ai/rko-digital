from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Recommendation:
    """Рекомендация банка с пояснением и ссылкой"""
    main_bank: str
    main_reason: str
    main_url: str
    backup_bank: Optional[str] = None
    backup_reason: Optional[str] = None
    backup_url: Optional[str] = None
    disclaimer: str = "Условия банка могут меняться, уточняйте детали при открытии счёта."


@dataclass
class UserAnswers:
    """Ответы пользователя на опрос"""
    business_status: str  # "has_entity", "planning", "self_employed"
    business_field: str  # "it", "freelance", "online_school", "shop", "agency", "other"
    monthly_turnover: str  # "under_100k", "100_300k", "300k_1m", "over_1m", "almost_none"
    foreign_payments: str  # "regular", "sometimes", "no"
    priority: str  # "cheap", "reliable", "simple", "foreign"
    need_acquiring: Optional[str] = None  # "yes", "no", "later"
    ready_to_register: Optional[str] = None  # "yes", "no"


def recommend_bank(answers: UserAnswers) -> Recommendation:
    """
    Основная логика рекомендации банка на основе ответов пользователя.
    Следует правилам из ТЗ.
    """
    
    # 1. Нет ИП/ООО и готов регистрироваться
    if answers.business_status == "planning" and answers.ready_to_register == "yes":
        if answers.priority in ["simple", "cheap"] or answers.business_field in ["it", "freelance"]:
            return Recommendation(
                main_bank="Альфа-Банк (регистрация + счёт)",
                main_reason="Регистрация бизнеса и счёт в одном пакете, простая онлайн-оформление для digital-специалистов",
                main_url="https://trk.ppdu.ru/click/8FDG8LXT?erid=2SDnjeEA46e",
                backup_bank="ВТБ (регистрация + счёт)",
                backup_reason="Крупный государственный банк, подойдёт если хотите солидный статус",
                backup_url="https://trk.ppdu.ru/click/SpRfgWha?erid=Kra23bNL5"
            )
        else:
            return Recommendation(
                main_bank="ВТБ (регистрация + счёт)",
                main_reason="Крупный государственный банк с полным пакетом регистрации бизнеса",
                main_url="https://trk.ppdu.ru/click/SpRfgWha?erid=Kra23bNL5",
                backup_bank="Альфа-Банк (регистрация + счёт)",
                backup_reason="Удобный онлайн-сервис для digital-предпринимателей",
                backup_url="https://trk.ppdu.ru/click/8FDG8LXT?erid=2SDnjeEA46e"
            )
    
    # 2. Самозанятый (НПД) без ИП
    if answers.business_status == "self_employed":
        return Recommendation(
            main_bank="Альфа-Банк (регистрация + счёт)",
            main_reason="Для работы с юрлицами обычно нужен расчётный счёт на ИП/ООО. Альфа предлагает регистрацию бизнеса и счёт в одном пакете",
            main_url="https://trk.ppdu.ru/click/8FDG8LXT?erid=2SDnjeEA46e",
            backup_bank="Точка",
            backup_reason="Когда оформите ИП — удобный онлайн-банк для digital-бизнеса",
            backup_url="https://trk.ppdu.ru/click/L7RmqL2g?erid=2SDnjdABGBD",
            disclaimer="Для самозанятых расчётный счёт обычно не требуется. Полноценный счёт для работы с юрлицами оформляется на ИП/ООО."
        )
    
    # 3. Есть ИП/ООО
    if answers.business_status == "has_entity":
        # Старт, малый оборот, "подешевле и онлайн"
        if (answers.monthly_turnover in ["under_100k", "almost_none", "100_300k"] and 
            answers.priority in ["cheap", "simple"]):
            return Recommendation(
                main_bank="Точка",
                main_reason="Оптимальный выбор для старта и малого оборота: низкие тарифы, всё онлайн, удобный интерфейс",
                main_url="https://trk.ppdu.ru/click/L7RmqL2g?erid=2SDnjdABGBD",
                backup_bank="Локо-Банк",
                backup_reason="Минимальные требования для совсем маленького оборота или редких операций",
                backup_url="https://trk.ppdu.ru/click/A9KwCptP?erid=Kra23ute7"
            )
        
        # Средний+ оборот, агентство, "крупный банк"
        if (answers.monthly_turnover in ["300k_1m", "over_1m"] or 
            answers.business_field == "agency" or 
            answers.priority == "reliable"):
            return Recommendation(
                main_bank="Альфа-Банк (только РКО)",
                main_reason="Крупный банк для среднего и большого оборота, надёжный партнёр для агентств и стабильного бизнеса",
                main_url="https://go.leadgid.ru/aff_c?aff_id=155793&offer_id=5289&p=adnetwork"
            )
        
        # Зарубежные оплаты важны
        if answers.foreign_payments in ["regular", "sometimes"] or answers.priority == "foreign":
            return Recommendation(
                main_bank="Альфа-Банк (только РКО)",
                main_reason="Один из лучших банков для работы с валютой и зарубежными платежами, широкие возможности ВЭД",
                main_url="https://go.leadgid.ru/aff_c?aff_id=155793&offer_id=5289&p=adnetwork",
                backup_bank="Точка",
                backup_reason="Также поддерживает валютные операции, уточняйте условия по ВЭД в банке",
                backup_url="https://trk.ppdu.ru/click/L7RmqL2g?erid=2SDnjdABGBD",
                disclaimer="Условия валютных операций и ВЭД могут различаться, уточняйте детали в выбранном банке."
            )
        
        # Регионы / запасной вариант
        if answers.business_field == "other" or answers.monthly_turnover == "almost_none":
            return Recommendation(
                main_bank="Ак Барс",
                main_reason="Надёжный региональный банк с хорошими условиями для малого бизнеса",
                main_url="https://trk.ppdu.ru/click/DEkn7EXf?erid=2SDnjecx1YU",
                backup_bank="Банк Санкт-Петербург",
                backup_reason="Стабильный банк с понятными тарифами",
                backup_url="https://trk.ppdu.ru/click/U8RDyGWj?erid=2SDnjeLA2cx"
            )
        
        # По умолчанию для ИП/ООО
        return Recommendation(
            main_bank="Точка",
            main_reason="Сбалансированный выбор для digital-бизнеса: хорошее сочетание цены, удобства и функционала",
            main_url="https://trk.ppdu.ru/click/L7RmqL2g?erid=2SDnjdABGBD",
            backup_bank="Альфа-Банк (только РКО)",
            backup_reason="Если нужен крупный банк с полным спектром услуг",
            backup_url="https://go.leadgid.ru/aff_c?aff_id=155793&offer_id=5289&p=adnetwork"
        )
    
    # 4. Планирует, но не готов регистрироваться сейчас
    if answers.business_status == "planning" and answers.ready_to_register == "no":
        return Recommendation(
            main_bank="Точка",
            main_reason="Когда будете готовы оформить ИП — удобный онлайн-банк для digital-бизнеса с низкими тарифами на старте",
            main_url="https://trk.ppdu.ru/click/L7RmqL2g?erid=2SDnjdABGBD",
            disclaimer="Для открытия расчётного счёта потребуется зарегистрировать ИП или ООО."
        )
    
    # Фолбэк (на всякий случай)
    return Recommendation(
        main_bank="Точка",
        main_reason="Универсальное решение для digital-бизнеса: низкие тарифы, удобный онлайн-банк",
        main_url="https://trk.ppdu.ru/click/L7RmqL2g?erid=2SDnjdABGBD",
        backup_bank="Альфа-Банк (только РКО)",
        backup_reason="Крупный банк с полным спектром услуг для бизнеса",
        backup_url="https://go.leadgid.ru/aff_c?aff_id=155793&offer_id=5289&p=adnetwork"
    )


def format_recommendation(recommendation: Recommendation) -> str:
    """Форматирует рекомендацию в читаемый текст для пользователя"""
    text = f"🏦 *{recommendation.main_bank}*\n\n"
    text += f"{recommendation.main_reason}\n\n"
    text += f"[Открыть счёт]({recommendation.main_url})\n\n"
    
    if recommendation.backup_bank:
        text += f"💡 *Запасной вариант — {recommendation.backup_bank}:*\n"
        text += f"{recommendation.backup_reason}\n"
        text += f"[Открыть счёт]({recommendation.backup_url})\n\n"
    
    text += f"📝 *Примечание:* {recommendation.disclaimer}"
    
    return text