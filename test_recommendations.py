#!/usr/bin/env python3
"""
Тестирование логики рекомендаций банков.
Запуск: python test_recommendations.py
"""

from bot.services.recommend import UserAnswers, recommend_bank, format_recommendation


def test_scenario(name: str, answers: UserAnswers):
    """Тестирование одного сценария"""
    print(f"\n{'='*60}")
    print(f"Сценарий: {name}")
    print(f"{'='*60}")
    
    print(f"Ответы: {answers}")
    
    recommendation = recommend_bank(answers)
    print(f"\nРекомендация: {recommendation.main_bank}")
    print(f"Причина: {recommendation.main_reason}")
    
    if recommendation.backup_bank:
        print(f"Запасной: {recommendation.backup_bank}")
    
    print(f"\nФорматированный текст:")
    text = format_recommendation(recommendation)
    # Убираем эмодзи для корректного вывода в консоли Windows
    text = text.replace('🏦 ', '').replace('💡 ', '').replace('📝 ', '')
    print(text)
    print(f"{'='*60}")


def main():
    """Тестирование 5 сценариев из ТЗ"""
    
    # 1. Нет ИП, готов регистрироваться
    test_scenario(
        "1. Нет ИП, готов регистрироваться (IT, малый оборот)",
        UserAnswers(
            business_status="planning",
            business_field="it",
            monthly_turnover="under_100k",
            foreign_payments="no",
            priority="simple",
            ready_to_register="yes"
        )
    )
    
    # 2. Есть ИП, малый оборот
    test_scenario(
        "2. Есть ИП, малый оборот (фриланс)",
        UserAnswers(
            business_status="has_entity",
            business_field="freelance",
            monthly_turnover="under_100k",
            foreign_payments="no",
            priority="simple"
        )
    )
    
    # 3. Есть ИП, агентство, средний оборот
    test_scenario(
        "3. Есть ИП, агентство, средний оборот",
        UserAnswers(
            business_status="has_entity",
            business_field="agency",
            monthly_turnover="300k_1m",
            foreign_payments="sometimes",
            priority="reliable"
        )
    )
    
    # 4. Самозанятый
    test_scenario(
        "4. Самозанятый (НПД)",
        UserAnswers(
            business_status="self_employed",
            business_field="other",
            monthly_turnover="almost_none",
            foreign_payments="no",
            priority="cheap"
        )
    )
    
    # 5. Нужны зарубежные платежи
    test_scenario(
        "5. Есть ИП, нужны зарубежные платежи",
        UserAnswers(
            business_status="has_entity",
            business_field="it",
            monthly_turnover="100_300k",
            foreign_payments="regular",
            priority="foreign"
        )
    )
    
    # 6. Планирует, но не готов регистрироваться
    test_scenario(
        "6. Планирует бизнес, но не готов регистрироваться",
        UserAnswers(
            business_status="planning",
            business_field="online_school",
            monthly_turnover="almost_none",
            foreign_payments="no",
            priority="cheap",
            ready_to_register="no"
        )
    )
    
    print("\nВсе сценарии протестированы!")


if __name__ == "__main__":
    main()